getal_1 = input("wat is het eerste getal?")
getal_2 = input("wat is het tweede getal?")
getal_3 = input("wat is het derde getal?")

x = float(getal_1)
y = float(getal_2)
z = float(getal_3)

if x > y:
    if x > z:
        print(f"{x} is het grootste getal")
    elif y > z:
        print(f"{y} is het grootste getal")
    else:
        print(f"{z} is het grooste getal")
elif y > z:
    print(f"{y} is het grootste getal")
else:
    print(f"{z} is het grooste getal")

