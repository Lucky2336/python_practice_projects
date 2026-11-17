import random

n = random.randint(1, 100)
guesses = 1
a = -1
while(a != n):
    a  =int(input("Guess the number between 1 and 100: "))
    if a < n:
         print("Too low! Try again.")
         guesses +=1
    elif a > n:
         print("Too high! Try again.")    
         guesses +=1

print(f"Congratulations! You guessed the number {n} in {guesses} attempts.")         