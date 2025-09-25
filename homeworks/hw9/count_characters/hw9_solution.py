# Подсчет количества букв

# На вход подается строка, например, "cccbba" результат работы программы -
# строка "c3b2a"
# Примеры для проверки работоспособности:


# def solution(text):
#     <you code here>
#
# assert solution("cccbba") == "c3b2a"
# assert solution("abeehhhhhccced") == "abe2h5c3ed"
# assert solution("aaabbceedd") == "a3b2ce2d2"
# assert solution("abcde") == "abcde"
# assert solution("aaabbdefffff") == "a3b2def5"


def count_char(text):
    result_string = ""
    current_symbol = text[0]
    count = 1
    for symbol in text[1:]:
        if symbol == current_symbol:
            count += 1
        else:
            result_string += current_symbol
            if count > 1:
                result_string += str(count)
            current_symbol = symbol
            count = 1
    result_string += current_symbol
    if count > 1:
        result_string += str(count)
    return result_string
