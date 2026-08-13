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

    name = input("What is your name? ").strip().title()
    color = input("Tell me a color: ").strip().lower()
    adj = input("Tell me an adjetive: ").strip().lower()
    goal = input("A goal you want tp achieve: ").strip().lower()

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}. ")

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally {goal}. ".upper())

if __name__=="__main__":
    main()
