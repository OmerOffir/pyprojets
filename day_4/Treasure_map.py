
'''
 In this screap we mark a 'X' on the map.
'''



row_1 = ["😍", "🥰", "😘"]
row_2 = ["😅", "😂", "🤣"]
row_3 = ["😈", "🥶", "🤢"]

map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")
position = input ("Where do you want to put the treasure ?  ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"



print(f"{row_1}\n{row_2}\n{row_3}")
