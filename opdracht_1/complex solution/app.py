from menu import Menu


class Main:

    def __init__(self):
        menu = Menu()
        while not menu.exit_program:
            menu.display_menu()
            menu.menu_option()


if __name__ == "__main__":
    main = Main()
