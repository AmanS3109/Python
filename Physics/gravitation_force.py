import math

G = 6.6784 * pow(10, -11)
mass1 = int(input("What is m1: "))
mass2 = int(input("What is m2: "))

radius = int(input("What's the distance between them : "))


def Force(mass1, mass2, radius):
    return G * ((mass1 * mass2) / (radius ** 2))


print(Force(mass1, mass2, radius))
