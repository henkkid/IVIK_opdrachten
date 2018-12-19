from print_options import Print_options
from party import Party
from pie import Pie
from controller import Controller

print_options = Print_options()
list_of_pies = []
list_of_pies.append(Pie("Chocolat delight", 10, 28))
list_of_pies.append(Pie("Bitter sweet story of vanilla", 8, 20))
list_of_pies.append(Pie("Black forrest extra vergance", 8, 18))


number_of_persons = print_options.display_float_question("aantal personen? ")
budget = print_options.display_float_question("wat is het budget? ")

party = Party(number_of_persons, budget)

controller = Controller(list_of_pies, party)

print_options.print_result(controller.process())
