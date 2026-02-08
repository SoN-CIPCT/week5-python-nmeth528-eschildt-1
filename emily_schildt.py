games = ("Banangrams", "Wingspan", "Cascadia", "Sagrada", "Monopoly", "Codenames")
print(games)
first_two = games[0:2]
print(f"The first two items in the list are: {first_two[0]}, {first_two[1]}")
middle_two = games[2:4]
print(f"The middle two items in the list are: {middle_two[0]}, {middle_two[1]}")
first_item = games[0]
last_item = games[-1]
print(f"The first and last items in the list are: {first_item}, {last_item}")

#Exercise 2
menu = ("Pizza", "Burgers", "Salad", "Steak", "Pasta")
for item in menu:
    print(item)
vegetarian_menu = ("Pizza", "Tacos", "Salad", "Tofu", "Pasta")
for item in vegetarian_menu:
    print(item)
    