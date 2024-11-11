def player_choice(player_num):
    print(f"Игрок {player_num}, выберите один из вариантов:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")
    choice = input("Введите 1, 2 или 3: ")
    if choice == '1':
        return "Камень"
    elif choice == '2':
        return "Ножницы"
    elif choice == '3':
        return "Бумага"
    else:
        print("Неверный ввод. Попробуйте снова.")
        return player_choice(player_num)


def determine_winner(player1, player2):
    if player1 == player2:
        return "Ничья!"
    elif (player1 == "Камень" and player2 == "Ножницы") or \
            (player1 == "Ножницы" and player2 == "Бумага") or \
            (player1 == "Бумага" and player2 == "Камень"):
        return "Игрок 1 победил!"
    else:
        return "Игрок 2 победил!"


def play_game():
    print("Добро пожаловать в игру Камень, Ножницы, Бумага!")

    player1_choice = player_choice(1)
    player2_choice = player_choice(2)

    print(f"Игрок 1 выбрал: {player1_choice}")
    print(f"Игрок 2 выбрал: {player2_choice}")

    result = determine_winner(player1_choice, player2_choice)
    print(result)


if __name__ == "__main__":
    play_game()