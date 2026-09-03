import random
def main():
   print("Hello what is your name? ")
   name = input()

   number = random.randit(1, 100)

   print("well, " + name + ", I am thinking of a number between 1 and 100.")

   guess = 0
   while guess != number:
      print("Take a guess")
      guess = int(input())

   if guess > number:
      print("Your guess is too high")
    elif guess < number:
      print ("your guess is too low")

      print("Good job, " + name + "! You guessed my number!")






if __name__=="__main__":
   main()
