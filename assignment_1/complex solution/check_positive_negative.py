class Check_negative_positve:

    def __init__(self):
        x = input("input number")
        try:
            self.x = float(x)
        except ValueError:
            print("input is not a number")
            Check_negative_positve()

    def Check(self):
        if self.x < 0:
            print("this is a negative number")
        elif self.x == 0:
            print("this number is zero")
        else:
            print("this number is positive")

        input("press enter to continue...")
