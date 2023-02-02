menu = {"cold_cofee": 40,
        "fride_rice": 70,
        "noodles": 80,
        "briyani": 110,
        "water": 10,
        "ice_cream":20}
cart =[]
total = 0
print("*----------MENU------------")
for key,values in menu.items():
    print(f"{key:10}:{values}")
print("****************************")

while True:
    food = input("select an item(q to quite): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"total is: {total}")
         
