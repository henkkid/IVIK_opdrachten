class Party:

    def __init__(self, number_of_persons, budget):
        self.number_of_persons = number_of_persons
        self.budget = budget
        self.left_over_money = budget
        self.left_over_pieces = 0
        self.cake_count = 0
        self.cost = 0

    def reset(self):
        self.left_over_pieces = 0
        self.cake_count = 0
        self.cost = 0

    def cake(self, pie):
        self.pie = pie
