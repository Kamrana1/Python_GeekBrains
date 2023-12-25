import json

file_path = 'companies.txt'

def calculate_profit(revenue, expenses):
    return revenue - expenses

try:
    firms_data = []
    total_profit = 0
    firms_profit = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                firm_name, ownership, revenue, expenses = parts
                revenue, expenses = map(float, (revenue, expenses))
                profit = calculate_profit(revenue, expenses)

                # Собираем информацию о прибыли каждой фирмы
                firms_profit[firm_name] = profit
                total_profit += profit

    # Вычисляем среднюю прибыль (исключая убыточные фирмы)
    profitable_firms_count = len([profit for profit in firms_profit.values() if profit > 0])
    average_profit = total_profit / profitable_firms_count if profitable_firms_count > 0 else 0

    # Создаем итоговый список
    result_list = [firms_profit, {"average_profit": average_profit}]

    # Сохраняем результат в виде JSON-объекта
    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=2)

    print("Итоговый список сохранен в result.json")

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")