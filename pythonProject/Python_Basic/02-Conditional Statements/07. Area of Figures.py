import math

figure = input()


if figure == 'square':
    side = float(input())
    print(side*side)
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    print(a*b)
elif figure=="circle":
    regius = float(input())
    print(math.pi*regius*regius)
elif figure == "triangle":
    side = float(input())
    hight = float(input())
    print(side*hight/2)