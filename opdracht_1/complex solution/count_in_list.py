class Count_in_list:

    def __init__(self):
        self.list = []
        self.counter = 0
        self.number_to_count = 0

    def get_numbers(self):
        for i in range(1, 11):
            getal = input(f"enter number {i}")
            try:
                self.list.append(float(getal))
            except ValueError:
                print("The value you entered is not a number")

        number_to_count = input("witch number should be counted?")

        try:
            self.number_to_count = float(number_to_count)
        except ValueError:
            print("The value you entered is not a number")

    def count_number(self):
        for number in self.list:
            if self.number_to_count == number:
                self.counter = self.counter + 1

    def print_solution(self):
        print(f"the number {self.number_to_count} exsist {self.counter} times in the list")
        input("press enter to continue...")


