# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
my_list = []
# Write your code below this row 👇
for num in position:
  my_list.append(num)
col = int(my_list[0])
row = int(my_list[1])
col -= 1
row -= 1

sel_row = map[row]
sel_row[col] = "X"
# print(col)
# print(row)

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
