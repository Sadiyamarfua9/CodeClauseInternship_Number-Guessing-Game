import random

secret_num=random.randint(1,150)
print("‼ Welcome to number guessing game ‼")

def number_guessing_game():
    print("You have 10 chances")
    for attempt in range(1,11):

        num=int(input("Enter your number between 1 and 150:\n"))
        attempt+=1

        if num < 1 and num > 150:
            print("Enter as valid number as per the instruction provided")
            continue       

        if num < secret_num:
            print("Hint: Your guessed number is too low")
        elif num > secret_num:
            print("Hint: Your guessed number is too high")
        else:
            print(f"Your guessed number is: {num} ✅")
            print(f"Computer's secret number is: {secret_num}")
            print(f"🎉🎉CONGRATULATIONS!!!!🎉🎉 You have won the game in {attempt} attempts")
            break

number_guessing_game()