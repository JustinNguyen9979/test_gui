import curses

def main_menu(stdscr):
    # Tắt chế độ hiển thị con trỏ
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
        height, width = stdscr.getmaxyx()
        title = "E-COMMERCE PACKING"
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, (width // 2) - (len(title) // 2), title)
        stdscr.attroff(curses.color_pair(1))

        # Vẽ menu
        for idx, item in enumerate(menu):
            x = (width // 2) - (len(item) // 2)
            y = 3 + idx
            if idx == selected_row:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, f"> {item} <")
                stdscr.attroff(curses.color_pair(2))
            else:
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
            stdscr.addstr(height - 2, 0, f"Bạn đã chọn: {menu[selected_row]}")
            stdscr.refresh()
            stdscr.getch()  # Chờ người dùng nhấn phím tiếp tục

# Thiết lập màu sắc và khởi chạy chương trình
def main():
    curses.wrapper(setup_curses)

def setup_curses(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Tiêu đề
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Mục đang chọn
    main_menu(stdscr)

if __name__ == "__main__":
    main()
