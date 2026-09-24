def main():
   times_table = 5

   print(f"Here is the {times_table} times table")

   for x in range (10,30):
      answer = x * times_table
      print(f"{x} times {times_table} is {answer}")

if __name__=="__main__":
   main()
