# I would first start by defining the main functio
#  txt file so i can have a bank of words after that
# create and define a function called start_game
#
import random

def main():
   start_game("words.txt")
def start_game(file):
    with open(file) as word_file:
       word = word_file.read().splitlines()
       print(random.choice(word))

if __name__=="__main__":
   main()
