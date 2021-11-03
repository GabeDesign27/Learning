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

# Write your code below this line 👇
import random

user_sel = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

com_choice_list = [rock, paper, scissors]

com_sel = random.randint(0, 2)

if user_sel == 0:
