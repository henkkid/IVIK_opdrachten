class Check_even_or_odd:

    def __init__(self):
        x = input("input number")
        try:
            self.x = float(x)
        except ValueError:
            print("input is not a number")
            Check_even_or_odd()

    def Check(self):
        remainder = self.x % 2
        if remainder == 1:
            print("the number is odd")
        else:
            print("the number is even")
        input("press enter to continue...")
