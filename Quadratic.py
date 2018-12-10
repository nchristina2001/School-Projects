import math

def qudeq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        print("The equation has real solutions")
        x_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

        print("x_1 = ", x_1)
        print("x_2 = ", x_2)
    else:
        print("The equation does not have real solutions")
count = "y"
while count =="y":
    a = float(input("Enter the value of a :"))
    b = float(input("Enter the value of b :"))
    c = float(input("Enter the value of c :"))

    qudeq(a, b ,c)
    count = input(" Enter y if continue, or n if not")
exit()
