import random
def main():
   print("Hello what is your name? ")
   name = input("")

   print(f"well, {name}, I am thinking of a number between 1 and 100.")

   number = random.randint(1, 100)
   guess = 0

   while guess != number:
      guess = int(input("take a guess: "))
      if guess > number:
         print("Your guess is too high")
      elif guess < number:
         print ("your guess is too low")

   print(f"Good job, {name}! You guessed my number!")


if __name__=="__main__":
   main()
