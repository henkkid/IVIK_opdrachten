class Calculator:

    def __init__(self):
        print("calculator")
        print("define the sum:")

        x = input("first number:")
        opperator = input("choose opperator(+-*/)")
        y = input("second number")

        calculation = Calculate(x, y)
        if not calculation.error:
            try:
                calculation.func[opperator](calculation)
                print(calculation.result)
            except KeyError:
                print("opperator not accepted")
        input("press enter to continue...")


class Calculate:
    result = 0
    error = False

    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            print("that is not a correct number")
            self.error = True

    def add(self):
        self.result = self.x + self.y

    def minus(self):
        self.result = self.x - self.y

    def multiply(self):
        self.result = self.x * self.y

    def defide(self):
        self.result = self.x / self.y

    func = {
        '+': add,
        '-': minus,
        '/': defide,
        '*': multiply
    }
