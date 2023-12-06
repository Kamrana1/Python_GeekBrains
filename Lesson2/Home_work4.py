str=input("Введите предложение: ")

str=str.split(" ")

i=0
while i< len(str):
    print(f"{i+1}. {str[i][:10]}")
    i+=1