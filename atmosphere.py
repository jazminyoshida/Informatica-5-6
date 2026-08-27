def main():

   layer = int(input("decent atmosphere layer : "))
   if layer == "Exoshere":
      print("yor altitude level will be from 700 to 10,000 km")
      a = int(input("Enter exact atitude: "))

   elif layer == "Thermosphere":
      print("Yor altitude level will be from 85 to 700 km")
      a = int(input("Enter exact atitude: "))

   elif layer == "Mesosphere":
      print("Your altitude level will be from 50 to 85 km")
      a = int(input("Enter exact atitude: "))

   elif layer == "Stratosphere":
      print("Your altitude level will be from 50 to 85 km")
      a = int(input("Enter exact atitude: "))


   else layer == "Troposphere":
      print("Your altitude level will be from 0 to 12 km")
      a = int(input("Enter exact atitude: "))



if __name__=="__main__":
   main()



