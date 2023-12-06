i=1
my_list=[]
while True:
    Productname=input("Введите название товара: ")
    Productprice=input("Введите цену товара: ")
    Productcount=input("Введите количество товара: ")
    Productunit=input("Введите единицу измерение: ")
    a = (i, {"Название: ":Productname,"Цена: ": Productprice,"Количество: ": Productcount,"Единица измерение: ": Productunit})
    my_list.append(a)
    print("Продолжить: 1")
    print("Выход: 2")
    i=int(input("Введите выбор: "))
    if i==2:
        break

for elem in my_list:
    print(f"{elem}")

prodnamelist=[]
for elem in my_list:
    for elem1 in elem[1]:
        prodnamelist.append(elem1[values])
