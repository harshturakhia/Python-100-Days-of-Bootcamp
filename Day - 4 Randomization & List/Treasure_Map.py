list1 = ["Q", "Q", "Q"]
list2 = ["Q", "Q", "Q"]
list3 = ["Q", "Q", "Q"]

map = [list1, list2, list3]
print(f"{list1}\n{list2}\n{list3}")

position = input("Where do you want to put the treasure ? ")

horizontal = int(position[0])
vertical = int(position[1])

print(map[vertical - 1])
