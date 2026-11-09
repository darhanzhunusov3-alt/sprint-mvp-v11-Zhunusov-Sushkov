# ===== T-1. Главное меню (общая задача) =====
TITLE = "Автосервис: запись"  # впишите название своего продукта
MENU = []  # пункты меню: (название, функция)


def ask_int(text):
    # спрашивает целое число, пока его не введут правильно
    while True:
        value = input(text).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Ошибка: введите целое число")


def ask_float(text):
    # спрашивает число (можно дробное), пока его не введут правильно
    while True:
        value = input(text).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")


def start():
    while True:
        print()
        print("=====", TITLE, "=====")
        for number, item in enumerate(MENU, start=1):
            print(number, "-", item[0])
        print("0 - Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            MENU[int(choice) - 1][1]()
        else:
            print("Нет такого пункта меню")

# ===== US-2. Свободное время =====
SLOTS = ["9:00", "10:00", "11:00", "12:00", "13:00",
         "14:00", "15:00", "16:00", "17:00"]
bookings = {}  # время -> запись клиента


def show_free():
    free = [slot for slot in SLOTS if slot not in bookings]
    if len(free) == 0:
        print("Свободного времени нет")
    else:
        print("Свободно:", ", ".join(free))


MENU.append(("Свободное время", show_free))

# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
