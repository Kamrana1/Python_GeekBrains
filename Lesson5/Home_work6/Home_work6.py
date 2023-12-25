file_path = 'subjects.txt'

subject_dict = {}  # Инициализация словаря для хранения данных

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                subject_name = parts[0].strip()
                lesson_types = parts[1].split()
                total_lessons = 0

                for lesson in lesson_types:
                    if '(' in lesson and ')' in lesson:
                        lesson_count = int(lesson[lesson.find('(')+1:lesson.find(')')])
                        total_lessons += lesson_count

                subject_dict[subject_name] = total_lessons
            elif line.strip():  # Проверка, что строка не пуста
                print(f"Пропущена строка с некорректным форматом: {line}")

    print("Словарь с общим количеством занятий:")
    print(subject_dict)

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    # asd