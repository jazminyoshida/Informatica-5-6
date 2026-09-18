def main():
    to_do = []
    answ = ""
    while answ != exit:

        print("What are your plans for the day?")
        answ = input("add, remove, daycomplete, exit\n: ").strip().lower()

        if answ == "add":
            print(to_do)
            add = input(" New Plans: ")
            where = int(input("what position? "))
            where -= 1
            to_do.insert(where, add)
            print("Item added to the list")

        elif answ == "remove":
            print(to_do)
            remove = input(" All Done: ")
            to_do.remove(remove)
            print("Item Removed")

        elif answ == "daycomplete":
            to_do.clear
            print("You have completed all items")

        elif answ == "exit":
            break

        print(to_do)




if __name__=="__main__":
   main()
