from math import ceil


def square(a):
    s = a*a
    return s


a = float(input("Введите сторону квадрата: "))
result = ceil(square(a))
print(result)