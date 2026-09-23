def main():
   user = input("Enter a number (1-10): ")

   user = int(user)

   print("Here is the", user, "times table")

   for i in range (1, 11):
      print(i, "times", user, "is", i * user)

if __name__=="__main__":
   main()
