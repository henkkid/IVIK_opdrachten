aantal_personen = float(input("number of persons"))
budget = float(input("budget?"))

number_of_chocolat_delight = aantal_personen // 10
left_over_chocolat_delight = 10 - (aantal_personen % 10)
if aantal_personen % 10 > 0:
    number_of_chocolat_delight = number_of_chocolat_delight + 1


number_of_bitter_sweet_story_of_vanilla = aantal_personen // 8
left_over_bitter_sweet_stroy_of_vanilla = 8 - (aantal_personen % 8)
if aantal_personen % 8 > 0:
    number_of_bitter_sweet_story_of_vanilla = number_of_bitter_sweet_story_of_vanilla + 1


number_of_black_forrest_extra_vergance = aantal_personen // 8
left_over_black_forrest_extra_vergance = 8 - (aantal_personen % 8)
if aantal_personen % 8 > 0:
    number_of_black_forrest_extra_vergance = number_of_black_forrest_extra_vergance + 1


cost_chocolat_delight = number_of_chocolat_delight * 28
cost_bitter_sweet_story_of_vanilla = number_of_bitter_sweet_story_of_vanilla * 20
cost_black_forrest_extra_vergance = number_of_black_forrest_extra_vergance * 18


print_all = True

if budget >= cost_chocolat_delight:
    print(f"you should buy {number_of_chocolat_delight} chocolat delight, this will cost you: {cost_chocolat_delight}")
    cost = cost_chocolat_delight
    left_over = left_over_chocolat_delight
elif budget >= cost_bitter_sweet_story_of_vanilla:
    print(f"you should buy {number_of_bitter_sweet_story_of_vanilla} bitter sweet story of vanilla, this will cost you: {cost_bitter_sweet_story_of_vanilla}")
    cost = cost_bitter_sweet_story_of_vanilla
    left_over = left_over_bitter_sweet_stroy_of_vanilla
elif budget >= cost_black_forrest_extra_vergance:
    print(f"you should buy {number_of_black_forrest_extra_vergance} black forrest extra vergance, this will cost you: {cost_black_forrest_extra_vergance}")
    cost = cost_black_forrest_extra_vergance
    left_over = left_over_black_forrest_extra_vergance
else:
    print("with this budget you can not feed your guest")
    print_all = False

if print_all:
    budget = budget - cost
    print (f"you will have {budget} left to spend")
    print(f"you will have {left_over} pieces left over")


