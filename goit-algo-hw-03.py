Перша задача
from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримання поточної дати
        current_date = datetime.today().date()
        # Розрахунок різниці між поточною датою та заданою датою
        difference = current_date - input_date
        # Повернення різниці у днях як цілого числа
        return difference.days
    except ValueError:
        # Обробка винятку у випадку неправильного формату вхідних даних
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

# Приклад використання:
print(get_days_from_today("2021-10-09"))  # Повинно вивести 157


Друга задача
import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка на відповідність вхідних параметрів обмеженням
    if not (1 <= minimum <= maximum <= 1000) or quantity > (maximum - minimum + 1):
        return []

    # Генерування унікальних випадкових чисел
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(minimum, maximum))

    # Повернення відсортованого списку чисел
    return sorted(list(numbers))

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Четверта задача
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження користувача з рядка в об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Визначення дати народження для поточного року
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув у поточному році, враховуємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Різниця між днем народження та сьогоднішнім днем
        days_until_birthday = (birthday_this_year - today).days
        
        # Перевірка, чи день народження випадає на наступний тиждень
        if 0 <= days_until_birthday <= 7:
            # Перенесення дати на понеділок, якщо день народження випадає на вихідний
            if (today + timedelta(days_until_birthday)).weekday() >= 5:
                days_until_birthday += (7 - (today + timedelta(days_until_birthday)).weekday())
            congratulation_date = today + timedelta(days_until_birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)