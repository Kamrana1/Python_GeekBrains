def int_func():
    str = input("Введите слово: ")
    result = []
    for i in str.split():
        result.append(i[0].upper()+i[1:])
    result = " ".join(result)
    return result;


print(int_func())