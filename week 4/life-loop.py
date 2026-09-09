import random
import time
def main():
    ideas = ["Cultural Backround", "historical centers" , "animals", "ect"]
    rndm = random.choices(ideas)
    time.sleep(1)
    print("Cant thinkof ideas for your essay? ")
    time.sleep(1)
    help = input("Do you need help? ").lower().strip()

    if help == "yes":
        print("Okay I got your back! ")
    else:
        print("Im going to help you anyways ")
    time.sleep(1)
    print("Heres an idea that might help you out ")
    time.sleep(1)
    print(rndm)
    time.sleep(1)
    help2 = input("Does this help? ").lower().strip()
    while help2 != "yes":
        help3 = input("Want another idea? ")
        if help3 == "yes":
            print("Here is another idea! ")
            rndm2 = random.choices(ideas)
            print(rndm2)

        else:
            time.sleep(1)
            print("Glad I could help! ")
            break
if __name__=="__main__":
   main()



