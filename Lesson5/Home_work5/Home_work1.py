file_path = 'numbers.txt'

# Программно создаем файл и записываем набор чисел
with open(file_path, 'w', encoding='utf-8') as file:
    numbers_to_write = [10, 20, 30, 40, 50]
    file.write(' '.join(map(str, numbers_to_write)))

# Считываем числа из файла и вычисляем их сумму
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        numbers = [int(number) for number in file.read().split()]
        sum_of_numbers = sum(numbers)
        print(f"Сумма чисел в файле: {sum_of_numbers}")
except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
except ValueError:
    print("Ошибка при чтении чисел из файла. Убедитесь, что файл содержит только числа, разделенные пробелами.")
except Exception as e:
    print(f"Произошла ошибка: {e}")