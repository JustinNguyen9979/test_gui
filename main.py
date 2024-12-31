import curses

def draw_menu(stdscr):
    # Danh sách các mục menu
    menu = [
        "1. Quét đơn hàng",
        "2. Tìm đơn hàng",
        "3. Xoá đơn hàng quá 30 ngày",
        "4. Đơn quét được trong ngày",
        "5. Thoát chương trình"
    ]
    current_idx = 0  # Mục hiện tại được chọn

    # Khởi tạo màu sắc
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # Mục được chọn
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Mục thông thường
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Tiêu đề
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Hướng dẫn
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)  # Viền khung
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Màu chữ menu

    while True:
        # Lấy kích thước màn hình
        height, width = stdscr.getmaxyx()
        stdscr.clear()

        # Hiển thị tiêu đề với viền đặc biệt
        title =     "╔════════════════════════════════╗"
        subtitle =  "║       E-COMMERCE-PACKING       ║"
        end_title = "╚════════════════════════════════╝"
        stdscr.addstr(1, (width - len(title)) // 2, title, curses.color_pair(3))
        stdscr.addstr(2, (width - len(subtitle)) // 2, subtitle, curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(3, (width - len(end_title)) // 2, end_title, curses.color_pair(3))

        # Hiển thị hướng dẫn
        instruction = "Dùng phím mũi tên ↑ ↓ để chọn, Enter để xác nhận, Q để quay lại, ESC để thoát."
        stdscr.addstr(5, (width - len(instruction)) // 2, instruction, curses.color_pair(4))

        # Tính toán kích thước menu và khung bao quanh
        menu_width = max(len(item) for item in menu) + 4
        menu_height = len(menu) + 4
        start_x = (width - menu_width) // 2
        start_y = (height - menu_height) // 2

        # Vẽ khung viền đúng cách
        stdscr.addstr(start_y - 1, start_x - 2, "╔" + "═" * (menu_width + 2) + "╗", curses.color_pair(5))
        for y in range(start_y, start_y + menu_height):
            stdscr.addstr(y, start_x - 2, "║", curses.color_pair(5))
            stdscr.addstr(y, start_x + menu_width, "║", curses.color_pair(5))
        stdscr.addstr(start_y + menu_height, start_x - 2, "╚" + "═" * (menu_width + 2) + "╝", curses.color_pair(5))

        # Hiển thị các mục menu, căn đều trên một đường thẳng
        for idx, item in enumerate(menu):
            x = start_x
            y = start_y + 1 + idx
            if idx == current_idx:
                stdscr.addstr(y, x, f"  {item}  ", curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(y, x, f"  {item}  ", curses.color_pair(6) | curses.A_BOLD)

        # Cập nhật màn hình
        stdscr.refresh()

        # Xử lý sự kiện bàn phím
        key = stdscr.getch()
        if key == curses.KEY_UP and current_idx > 0:
            current_idx -= 1
        elif key == curses.KEY_DOWN and current_idx < len(menu) - 1:
            current_idx += 1
        elif key == ord('\n'):  # Nhấn Enter
            return current_idx  # Trả về mục được chọn
        elif key == ord('q'):  # Nhấn Q để quay lại menu
            return -2  # Quay lại trang trước
        elif key == 27:  # Nhấn ESC để thoát chương trình
            return -1

def sub_menu(stdscr):
    # Ví dụ về một menu con
    menu_items = [
        "Quét đơn hàng",
        "Tìm đơn hàng",
        "Xoá đơn hàng quá 30 ngày",
        "Đơn quét được trong ngày",
        "Quay lại"
    ]
    current_idx = 0  # Mục hiện tại được chọn

    while True:
        # Lấy kích thước màn hình
        height, width = stdscr.getmaxyx()
        stdscr.clear()

        # Hiển thị tiêu đề
        stdscr.addstr(1, (width - len("SUB MENU")) // 2, "SUB MENU", curses.A_BOLD | curses.color_pair(3))
        stdscr.addstr(3, (width - len("Quay lại")) // 2, "Quay lại bằng phím 'q'", curses.color_pair(4))

        # Hiển thị các mục menu
        for idx, item in enumerate(menu_items):
            if idx == current_idx:
                stdscr.addstr(5 + idx, (width - len(item)) // 2, item, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(5 + idx, (width - len(item)) // 2, item, curses.color_pair(6) | curses.A_BOLD)

        stdscr.refresh()

        # Xử lý sự kiện bàn phím
        key = stdscr.getch()
        if key == curses.KEY_UP and current_idx > 0:
            current_idx -= 1
        elif key == curses.KEY_DOWN and current_idx < len(menu_items) - 1:
            current_idx += 1
        elif key == ord('\n'):  # Nhấn Enter
            return current_idx
        elif key == ord('q'):  # Nhấn Q để quay lại menu chính
            return -1
        elif key == 27:  # Nhấn ESC để thoát
            return -1

def main():
    curses.wrapper(run)

def run(stdscr):
    # Vẽ menu chính
    while True:
        selected_option = draw_menu(stdscr)
        stdscr.clear()

        if selected_option == -1:
            # Thoát chương trình
            message = "Đã thoát chương trình."
            break
        elif selected_option == -2:
            # Quay lại menu chính
            continue
        else:
            # Vào menu con
            sub_menu_option = sub_menu(stdscr)
            stdscr.clear()

            if sub_menu_option == -1:
                continue

            # Hiển thị kết quả
            message = f"Bạn đã chọn: {sub_menu_option + 1}. Còn lại các hành động sẽ được xử lý."

        height, width = stdscr.getmaxyx()
        x = (width - len(message)) // 2
        y = height // 2
        stdscr.addstr(y, x, message, curses.color_pair(3) | curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()  # Chờ nhấn phím để kết thúc

if __name__ == "__main__":
    main()
