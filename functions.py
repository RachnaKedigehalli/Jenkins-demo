import math

def multiply(a, b):
    return a * b

def square(a):
    return multiply(a, a)

def circle_perimeter(r):
    if r >= 0:
        return multiply(multiply(2, math.pi), r)
    return 0

def circle_area(r):
    if r>= 0:
        return multiply(math.pi, square(r))
    return 0

if __name__ == '__main__':
    print("Circle of radius 3:\n")
    print("Perimeter:", circle_perimeter(3))
    print("Area:", circle_area(3))