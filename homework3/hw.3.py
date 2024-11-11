from datetime import datetime


def get_age():
    while True:
        try:
            birth_date_str = input("Введите вашу дату рождения (дд/мм/гггг): ")

            day, month, year = map(int, birth_date_str.split('/'))

            birth_date = datetime(year, month, day)

            today = datetime.today()

            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1

            print(f"Ваш возраст: {age} лет.")
            break

        except ValueError:
            print(
                "Неверный формат даты или недопустимые значения. Пожалуйста, вводите только числа в формате дд/мм/гггг.")
        except Exception as e:

            print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")


get_age()