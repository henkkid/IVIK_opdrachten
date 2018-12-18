class CheckLargest:

    def __init__(self):
        x = input("first number")
        try:
            self.x = float(x)
        except ValueError:
            print("the input is not a number")
            CheckLargest()
        y = input("second number")
        try:
            self.y = float(y)
        except ValueError:
            print("the input is not a number")
            CheckLargest()
        z = input("third number")
        try:
            self.z = float(z)
        except ValueError:
            print("the input is not a number")
            CheckLargest()

    def Check(self):
        if self.x > self.y:
            if self.x > self.z:
                print(f"{self.x} is the largest number")
            else:
                print(f"{self.z} is the largest number")
        elif self.y > self.z:
            print(f"{self.y} is the largest number")
        else:
            print(f"{self.z} is the largest number")

