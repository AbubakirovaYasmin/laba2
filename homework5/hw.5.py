def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

odd_numbers = get_number()

odd_list = list(odd_numbers)

if len(odd_list) >= 5:
    print(f"Первое нечетное число: {odd_list[0]}")
    print(f"Пятое нечетное число: {odd_list[4]}")
    print(f"Последнее нечетное число: {odd_list[-1]}")
else:
    print("Недостаточно нечетных чисел в диапазоне.")