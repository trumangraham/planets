from planetarium1 import planet

mercury = planet("Mercury", "hot", 1, 330)
venus = planet("Venus", "small", 2, 132)
earth = planet("Earth", "habitable", 1, 76)
mars = planet("Mars", "red", 2, 53)
jupiter = planet("Jupiter", "big", 12, -19)
saturn = planet("Saturn", "ringy", 4, -78)
uranus = planet("Uranus", "gasy", 3, -219)
neptune = planet("Neptune", "blue", 7, -347)


p = input("Would you like to see some planets?")

while (p != 'no'):
    print()
    print("1: Mercury")
    print("2: Venus")
    print("3: Earth")
    print("4: Mars")
    print("5: Jupiter")
    print("6: Saturn")
    print("7: Uranus")
    print("8: Neptune")
    
    print()
    choice = input("Which one would you like to see?")
    print()
    if(choice == "1"):
        print(mercury)
    if(choice == "2"):
        print(venus)
    if(choice == "3"):
        print(earth)
    if(choice == "4"):
        print(mars)
    if(choice == "5"):
        print(jupiter)
    if(choice == "6"):
        print(saturn)
    if(choice == "7"):
        print(uranus)
    if(choice == "8"):
        print(neptune)


    

    
    



