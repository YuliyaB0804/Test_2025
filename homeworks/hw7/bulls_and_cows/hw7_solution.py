# Быки и коровы
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с
# неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает
# первую попытку отгадать число. Попытка — это 4-значное число с
# неповторяющимися цифрами, сообщаемое противнику. Противник сообщает в ответ,
# сколько цифр угадано без совпадения с их позициями в тайном числе (то есть
# количество коров) и сколько угадано вплоть до позиции в тайном числе (то
# есть количество быков). При игре против компьютера игрок вводит комбинации
# одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и
# коровы"
# Пример
# Загадано число 3219
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!


import random


def generate_secret_number():
    digits = list('0123456789')
    random.shuffle(digits)
    # Первое число не должно быть 0
    if digits[0] == '0':
        for i in range(1, 10):
            # Проверяем первый элемент, если он 0, то меняем местами с первым отличным от 0 числом
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(digits[:4])


def check_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows


def main():
    secret = generate_secret_number()
    print("Загадано число из 4 уникальных цифр.")
    # Для удобства тестирования можно раскомментировать ниже
    # print(f"Секрет (для отладки): {secret}")

    while True:
        guess = input("Введите число: ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Ошибка: введите 4 разные цифры")
            continue

        bulls, cows = check_guess(secret, guess)

        if bulls == 4:
            print("Вы выиграли!")
            break

        # Формируем правильное окончание для «быков» и «коров»
        def plural(number, one, few, many):
            if 11 <= number % 100 <= 14:
                return many
            elif number % 10 == 1:
                return one
            elif 2 <= number % 10 <= 4:
                return few
            else:
                return many

        parts = []
        if cows > 0:
            parts.append(f"{cows} {plural(cows, 'корова', 'коровы', 'коров')}")
        if bulls > 0:
            parts.append(f"{bulls} {plural(bulls, 'бык', 'быка', 'быков')}")

        print(', '.join(parts) if parts else "Нет совпадений")


if __name__ == "__main__":
    main()
