number = int(input("Ededi daxil edin: "))
num=number
maximum= number%10



while number>0:
    digit=number%10
    if digit>maximum:
        maximum=digit

    if digit == 9:
        break

    number//=10
    print(number)

print(f"{num} Ededinin maksimumu {maximum}")