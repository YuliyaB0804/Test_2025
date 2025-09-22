# Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным). И проверяющей может ли такая карта
# существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания Алгоритм Луна
# Примеры
# def solution(number):
#     ...
#
# assert solution(4561261212345464) == False
# assert solution(4561261212345467) == True
# https: // www.paypalobjects.com / en_GB / vhelp / paypalmanager_help /
# credit_card_numbers.htm


def is_card_number_valid(number):
    number = str(number)
    if not number.isdigit() or len(number) == 0:
        return False
    total = 0
    reverse_digits = number[::-1]
    for i,digit in enumerate(reverse_digits):
        res = int(digit)
        if i % 2 == 1:
            res *= 2
            if res > 9:
                res -= 9
        total += res
    return total % 10 == 0
