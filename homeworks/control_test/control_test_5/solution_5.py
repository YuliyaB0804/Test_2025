phase = input("Введите число:")


def number_palindrom(number):
    if number[::-1] == number:
        return True
    return False


print(number_palindrom(phase))
