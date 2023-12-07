def divide(a, b):
    if b!=0:
        return a/b
    else:
        return "Нельзя делить на ноль"

x = int(input("Введите число: "))
y = int(input("Введите число: "))

print(divide(x,y))
