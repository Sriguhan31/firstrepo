import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Let the user guess up to 3 times
print("I'm thinking of a number between 1 and 10.")
for attempt in range(3):
    guess = int(input("Take a guess: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"❌ Sorry! The number was {secret_number}. Better luck next time!")
