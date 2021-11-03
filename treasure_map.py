row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

my_list = []
for num in position:
  my_list.append(num)
col = int(my_list[0])
row = int(my_list[1])
col -= 1
row -= 1

sel_row = map[row]
sel_row[col] = "X"

print(f"{row1}\n{row2}\n{row3}")
