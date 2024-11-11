import random


def find_multiples():
    numbers = [random.randint(0, 200) for _ in range(10)]
    numbers.sort()
    print("Сгенерированные числа:", numbers)

    while True:
        try:
            x = int(input("Введите цифру X, кратные которой необходимо найти: "))

            if x < 1 or x > 9:
                print("Введите число от 1 до 9.")
                continue

            multiples = list(filter(lambda num: num % x == 0, numbers))
            multiples.sort()

            if multiples:
                print(f"Числа, кратные {x}: {multiples}")
            else:
                print(f"Нет чисел, кратных {x}.")
            break

        except ValueError:
            print("Неверный ввод! Пожалуйста, введите число.")


find_multiples()