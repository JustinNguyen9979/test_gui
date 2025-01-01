import curses
import pyfiglet

def display_title(stdscr):
    """Hiển thị tiêu đề với khung viền và thông tin tác giả."""
    height, width = stdscr.getmaxyx()
    title = pyfiglet.figlet_format("E-COMMERCE PACKING")
    lines = title.splitlines()

    # Tính toán kích thước khung viền
    max_line_length = max(len(line) for line in lines)
    box_width = max_line_length + 4
    box_height = len(lines) + 4

    start_x = (width - box_width) // 2
    start_y = 1

    # Vẽ khung viền
    for y in range(start_y, start_y + box_height):
        for x in range(start_x, start_x + box_width):
            if y == start_y or y == start_y + box_height - 1:
                stdscr.addch(y, x, '-' if x > start_x and x < start_x + box_width - 1 else '+')
            elif x == start_x or x == start_x + box_width - 1:
                stdscr.addch(y, x, '|')

    # Hiển thị tiêu đề bên trong khung
    for i, line in enumerate(lines):
        x = start_x + 2 + (box_width - 4 - len(line)) // 2
        y = start_y + 2 + i
        stdscr.addstr(y, x, line, curses.color_pair(1))  # Sử dụng màu cặp 1 (xanh lá cây)

    # Hiển thị thông tin tác giả bên dưới khung
    author_info = "Designed by: Justin Nguyen | WhatsApp: 0982.579.098"
    stdscr.addstr(start_y + box_height, (width - len(author_info)) // 2, author_info, curses.color_pair(3))  # Sử dụng màu cặp 2 (đỏ)

def main_menu(stdscr):
    """Hiển thị menu chính và xử lý điều hướng."""
    curses.curs_set(0)

    # Danh sách menu
    menu = [
        "Quét đơn hàng",
        "Check mã vận đơn",
        "Xoá đơn hàng quá 30 ngày",
        "Hiển thị đơn đã đóng trong ngày",
        "Thoát",
    ]
    selected_row = 0

    while True:
        # Xóa màn hình trước khi vẽ lại
        stdscr.clear()

        # Hiển thị tiêu đề
        display_title(stdscr)

        # Vẽ menu
        height, width = stdscr.getmaxyx()
        title_height = len(pyfiglet.figlet_format("E-COMMERCE PACKING").splitlines()) + 6
        for idx, item in enumerate(menu):
            x = (width // 2) - (len(item) // 2)
            y = title_height + 2 + idx
            if idx == selected_row:
                # Dòng được chọn in đậm và đổi màu chữ xanh
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(y, x, f"> {item} <")
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                # Dòng không được chọn hiển thị bình thường
                stdscr.addstr(y, x, item)

        stdscr.refresh()

        # Xử lý phím bấm
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row > 0:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(menu) - 1:
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
            if selected_row == len(menu) - 1:  # Thoát
                break
            stdscr.addstr(height - 2, 0, f"Bạn đã chọn: {menu[selected_row]}", curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()  # Chờ người dùng nhấn phím tiếp tục

# Thiết lập màu sắc và khởi chạy chương trình
def main():
    curses.wrapper(setup_curses)

def setup_curses(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Cặp màu 1: xanh lá cây, đen
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Cặp màu 2: đỏ, đen
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)   # Cặp màu 3: xanh dương, đen
    main_menu(stdscr)

if __name__ == "__main__":
    main()
