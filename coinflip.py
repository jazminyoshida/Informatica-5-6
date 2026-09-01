import random

def main():

    flip = input("Heads(1) or Tails(2): ")
    coin = random.randint(1,2)

    if coin == 1:
        print("heads")
    else:
        print("tails")

    if flip == coin:
        print("you win!")
    else:
        print("you loose")


if __name__=="__main__":
   main()
