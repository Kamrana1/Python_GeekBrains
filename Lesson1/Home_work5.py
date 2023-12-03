revenue = int(input("Введите вырочку: "))
expense = int(input("Введите издержку: "))

profit = revenue - expense

if profit>0:
    print(f"Ваш прибыль составлает {profit}")
elif profit<0:
    print(f"Ваш убыток составлет {profit}")
else:
    print("Вы ничего не заработали")
