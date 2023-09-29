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

#Write your code below this line 👇
print("Welcome to the rock, paper, scissors simulator!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for scissors. "))
import random
computer_choice = random.randint(0, 2)
print("You chose:")
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
else:
  print("That's not rock, paper, or scissors! Try again!")

print("Computer Chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

combined_choice = [user_choice, computer_choice]
if combined_choice == [0, 0]:
  print("Draw")
elif combined_choice == [0, 1]:
  print("You lose")
if combined_choice == [0, 2]:
  print("You Win!")
elif combined_choice == [1, 0]:
  print("You win!")
elif combined_choice == [[1, 1]]:
  print("Draw!")
elif combined_choice == [1, 2]:
  print("You lose!")
elif combined_choice == [2, 0]:
  print("You lose!")
elif combined_choice == [2, 1]:
  print("You win!")
elif combined_choice == [2, 2]:
  print("Draw")