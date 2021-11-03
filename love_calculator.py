print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

check1 = "TRUE"
check2 = "LOVE"
score1 = 0
score2 = 0
score = ""
for let in check1.lower():
    for na in name1.lower():
        if let == na:
            # debug check for letter count
            #     print(f"{let} occurs 1 time")
            score1 += 1
    for na in name2.lower():
        if let == na:
            score1 += 1
# debug check for iteration of loop
# else:
# print ("No matches found.")

for let in check2.lower():
    for na in name1.lower():
        if let == na:
            # debug check for letter count
            #     print(f"{let} occurs 1 time")
            score2 += 1
    for na in name2.lower():
        if let == na:
            # debug check for letter count
            #     print(f"{let} occurs 1 time")
            score2 += 1
# debug check for iteration of loop

# print(f"The total score is {score}")
score = str(score1) + str(score2)
scoreint = int(score)

if scoreint < 10 or scoreint > 90:
    print(f"Your score is {score}, you go together like mentos and coke.")
elif scoreint > 40 and scoreint < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"your score is {score}.")
