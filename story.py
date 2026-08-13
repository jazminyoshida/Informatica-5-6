def main():
    # planet=input("Planet:")

    # # Separation
    # print("Hello", planet)

    # # concatonation
    # print("Hello " + planet)

    # # Formated Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ")
    color = input("Tell me a color: ")
    adj = input("Tell me an adjetive: ")
    goal = input("A goal you want tp achieve: ")

    print(f"Hello, {name}!", end="\n\n")

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}.")

if __name__=="__main__":
    main()
