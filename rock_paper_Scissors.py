import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_sel = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
choice_list = [rock, paper, scissors]

com_sel = random.randint(0, 2)

if user_sel == "0":
    user_choice = choice_list[0]
elif user_sel == "1":
    user_choice = choice_list[1]
else:
    user_choice = choice_list[2]
    
if com_sel == 0:
    com_choice = choice_list[0]
elif com_sel == 1:
    com_choice = choice_list[1]
else:
    com_choice = choice_list[2]

if int(user_sel) > com_sel:
    print(f"You chose {user_choice}, the computer chose {com_choice}. You win!")
elif int(user_sel) == com_sel:
    print(f"You chose {user_choice}, the computer chose {com_choice}. It's a tie! ")
else:
    print(f"You chose {user_choice}, the computer chose {com_choice}. You lost!")
    
