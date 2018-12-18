from calculator import Calculator
from check_positive_negative import Check_negative_positve
from check_even_or_odd import Check_even_or_odd
from Check_Largest import CheckLargest
from count_in_list import Count_in_list

class Menu:

    def __init__(self):
        self.menuoptions = {
            1: self.calculator,
            2: self.check_positive,
            3: self.check_even,
            4: self.check_largest,
            5: self.check_exists,
            6: self.exit
        }

        self.exit_program = False

    def display_menu(self):
        print("""
            what whould you like to run?
            1. Calculator
            2. Check if number is positive, negative of zero
            3. Check if number is even or odd
            4. Check witch number is the largest of three inputs
            5. Check how many times a number exists in a list of numbers
            6. Exit
            """)

    def menu_option(self):
        answer = input("your choice(1,2,3,4,5 or 6)?")
        try:
            self.menuoptions[int(answer)]()
        except ValueError:
            print("this is not a correct input, fill in 1 of the menu options")
            self.menu_option()

    def calculator(self):
        Calculator()

    def check_positive(self):
        check_negative_positive = Check_negative_positve()
        check_negative_positive.Check()

    def check_even(self):
        check_even_or_odd = Check_even_or_odd()
        check_even_or_odd.Check()

    def check_largest(self):
        check_largest = CheckLargest()
        check_largest.Check()

    def check_exists(self):
        count_in_list = Count_in_list()
        count_in_list.get_numbers()
        count_in_list.count_number()
        count_in_list.print_solution()

    def exit(self):
        self.exit_program = True
