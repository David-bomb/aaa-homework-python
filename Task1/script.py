import csv

DATA_FILE = "Corp_Summary.csv"
OUTPUT_REPORT_FILE = "report.csv"


def load_data(filename):
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []
    return data


def display_team_hierarchy(data):
    if not data:
        print("Данные для отображения иерархии отсутствуют.")
        return

    departments = {}
    for row in data:
        department = row.get('Департамент')
        team = row.get('Отдел')
        if department and team:
            if department not in departments:
                departments[department] = set()
            departments[department].add(team)

    print("\n--- Иерархия команд ---")
    for department, teams in sorted(departments.items()):
        print(f"Департамент: {department}")
        for team in sorted(list(teams)):
            print(f"  - Команда: {team}")
    print("------------------------")


def generate_department_summary(data):
    if not data:
        print("Данные для генерации отчёта отсутствуют.")
        return []

    department_stats = {}
    for row in data:
        department = row.get('Департамент')
        salary_str = row.get('Оклад')

        if department and salary_str:
            try:
                salary = int(salary_str)
            except ValueError:
                continue

            if department not in department_stats:
                department_stats[department] = {
                    'Численность': 0,
                    'Минимальная зарплата': float('inf'),
                    'Максимальная зарплата': float('-inf'),
                    'Общая зарплата': 0
                }

            stats = department_stats[department]
            stats['Численность'] += 1
            stats['Минимальная зарплата'] = min(stats['Минимальная зарплата'], salary)
            stats['Максимальная зарплата'] = max(stats['Максимальная зарплата'], salary)
            stats['Общая зарплата'] += salary

    summary_report = []
    for department, stats in sorted(department_stats.items()):
        avg_salary = stats['Общая зарплата'] / stats['Численность'] if stats['Численность'] > 0 else 0
        summary_report.append({
            'Название департамента': department,
            'Численность': stats['Численность'],
            'Вилка зарплат': f"{stats['Минимальная зарплата']} - {stats['Максимальная зарплата']}",
            'Средняя зарплата': f"{round(avg_salary, 2)}",
        })
    return summary_report


def display_department_summary(summary_report):
    if not summary_report:
        print("Сводный отчёт пуст.")
        return

    print("\n--- Сводный отчёт по департаментам ---")
    for row in summary_report:
        print(f"Департамент: {row['Название департамента']}")
        print(f"  Численность: {row['Численность']}")
        print(f"  Вилка зарплат: {row['Вилка зарплат']}")
        print(f"  Средняя зарплата: {row['Средняя зарплата']}")
        print("-" * 30)
    print("---------------------------------------")


def save_department_summary_to_csv(summary_report, filename):
    if not summary_report:
        print("Нет данных для сохранения в отчёт.")
        return

    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            fieldnames = list(summary_report[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(summary_report)
        print(f"Сводный отчёт успешно сохранен в '{filename}'")
    except Exception as e:
        print(f"Произошла ошибка при сохранении отчёта: {e}")


def main_menu():
    data = load_data(DATA_FILE)
    if not data:
        print("Не удалось загрузить данные. Завершение программы.")
        return

    while True:
        print("\n--- Главное меню ---")
        print("1. Вывести иерархию команд")
        print("2. Вывести сводный отчёт по департаментам")
        print("3. Сохранить сводный отчёт в CSV-файл")
        print("4. Выйти")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == '1':
            display_team_hierarchy(data)
        elif choice == '2':
            summary = generate_department_summary(data)
            display_department_summary(summary)
        elif choice == '3':
            summary = generate_department_summary(data)
            save_department_summary_to_csv(summary, OUTPUT_REPORT_FILE)
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 4.")



main_menu()