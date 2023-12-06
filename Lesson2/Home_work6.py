i = 1
my_list = []

while True:
    Productname = input("Введите название товара: ")
    Productprice = float(input("Введите цену товара: "))  # Преобразуем в число
    Productcount = int(input("Введите количество товара: "))  # Преобразуем в число
    Productunit = input("Введите единицу измерения: ")

    a = (i, {"name": Productname, "price": Productprice, "count": Productcount, "unit": Productunit})
    my_list.append(a)

    print("Продолжить: 1")
    print("Выход: 2")
    i = int(input("Введите выбор: "))

    if i == 2:
        break

for elem in my_list:
    print(f"{elem}")

prodnamelist = []
prodpricelist=[]
prodcountlist=[]
productunitlist=[]

for elem in my_list:
    prodnamelist.append(elem[1]["name"])
    prodpricelist.append(elem[1]["price"])
    prodcountlist.append(elem[1]["count"])
    productunitlist.append(elem[1]["unit"])

my_dict = {}
my_dict["name"] = prodnamelist
my_dict["price"] = prodpricelist
my_dict["count"] = prodcountlist
my_dict["unit"] = productunitlist

print(my_dict)