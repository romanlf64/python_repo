from math import ceil

n = float(input("Длина стороны квадрата: "))

def square(n):
    return (n ** 2)

print("Площадь квадрата, округлённая в большую сторону:", ceil(square(n)))