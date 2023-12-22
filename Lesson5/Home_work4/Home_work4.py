translation_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

input_file_path = 'input.txt'
output_file_path = 'output.txt'

try:
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                parts = line.split(' — ')
                if len(parts) == 2:
                    english_number, value = parts
                    russian_number = translation_dict.get(english_number.strip(), english_number.strip())
                    output_file.write(f"{russian_number} — {value}")
except FileNotFoundError:
    print(f"Файл '{input_file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")