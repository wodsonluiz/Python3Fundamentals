menus = [["Egg Sandwich", "Bagel", "Coffe"], ["Soup", "Salad"]]

print(menus[0][2])

menusWithDictionary = {"Breakfast": ["Coffe", "Bagel"],
                       "Lunch": ["Turkey Sandwich", "BLT"],
                       "Dinner": ["Soup", "Salad"]}

print("Breakfast menu: \t", menusWithDictionary["Breakfast"])
print("Lunch menu \t", menusWithDictionary["Lunch"])
print("Diner menu \t", menusWithDictionary["Dinner"])

# With loop
for name, meunu in menusWithDictionary.items():
    print(name, ":", meunu)