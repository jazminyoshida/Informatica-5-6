def main():

   layer = int(input("decnt atmosphere layer : "))
   if layer == "Exoshere":
      print("yor altitude level will be from 700 to 10,000 km")
      

   elif layer == "Thermosphere":
      print("Yor altitude level will be from 85 to 700 km")

   elif layer == "Mesosphere":
      print("Your altitude level will be from 50 to 85 km")

   elif layer == "Stratosphere":
      print("Your altitude level will be from 50 to 85 km")

   else layer == "Troposphere":
      print("Your altitude level will be from 0 to 12 km")


if __name__=="__main__":
   main()
