import random

correct_num = random.randint(0,20)

print(correct_num)

#print(correct_num)
user_guess = int(input("What is your guess? "))

while correct_num != user_guess:
    if user_guess < correct_num:
        print("Too Low")
    else:
        print("Too High")
    user_guess = int(input("What is your guess? "))

print("You got it!")
