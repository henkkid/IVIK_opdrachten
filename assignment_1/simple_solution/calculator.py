def add(x, y):
    anser = x + y
    return anser


def minus(x, y):
    anser = x - y
    return anser


def multiply(x, y):
    anser = x * y
    return anser

def defide(x, y):
    anser = x / y
    return anser


operators = {
    '+': add,
    '-': minus,
    '*': multiply,
    '/': defide
}

getal_1 = input("wat is het eerste getal?")
getal_2 = input("wat is het tweede getal?")
functie = input("type functie (+ - * /)?")


x = float(getal_1)

y = float(getal_2)

anser = operators[functie](x, y)

print(anser)



