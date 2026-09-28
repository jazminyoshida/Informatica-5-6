def main():
   not_validated = True

   while not_validated: #condition
        try:
            int(input("Enter a number between 1 and 10: "))
            not_validated = False
        except ValueError:
            print("You must enter a number between 1 and 10.")
        if number < 1 or number > 10:
            not_validated = True


if __name__=="__main__":
   main()
