from planetarium1 import planet

mercury = planet("Mercury", "hot", 1, 330)
venus = planet("Venus", "small", 2, 132)
earth = planet("Earth", "habitable", 1, 76)
mars = planet("Mars", "red", 2, 53)
jupiter = planet("Jupiter", "big", 12, -19)
saturn = planet("Saturn", "ringy", 4, -78)
uranus = planet("Uranus", "gasy", 3, -219)
neptune = planet("Neptune", "blue", 7, -347)


print("What planet would you like to see?")
p = input()

if(p == "mercury"):
    print(mercury)
if(p == "venus"):
    print(venus)
if(p == "earth"):
    print(earth)
if(p == "mars"):
    print(mars)
if(p == "jupiter"):
    print(jupiter)
if(p == "saturn"):
    print(saturn)
if(p == "uranus"):
    print(uranus)
if(p == "neptune"):
    print(neptune)
    

    
    



