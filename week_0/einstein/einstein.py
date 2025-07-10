def einstein():
    mass = int(input("m: "))
    print("E:", energy(mass))
    
def energy(mass):
    return mass * (3 * 10**8) ** 2

einstein()
    