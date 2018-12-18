list = []

for i in range(1, 11):
    getal = input(f"vul getal {i} in")
    list.append(getal)

list_getallen = []

for item in list:
    list_getallen.append(float(item))

controle_getal = input("welk getal wil u tellen?")

x = float(controle_getal)

teller = 0

for getal in list_getallen:
    if getal == x:
        teller = teller + 1

print(teller)