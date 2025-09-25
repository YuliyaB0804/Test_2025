# Строки с заданным символом

# Напишите программу, которая бы работала следующим образом - находила символ
# "#" и если этот символ найден - удаляла предыдущий символ из строки. Ваша
# задача обработать строки с "#" символом.
# Примеры:
# def solution(text):
#     <you code here>


# assert solution("a#bc#d") == "bd"
# assert solution("abc#d##c") == "ac"
# assert solution("abc##d######") == ""
# assert solution("#######") == ""
# assert solution("") == ""


def remove_previous_symbol(raw_str):
    result_string = ""
    i = 0
    while i < len(raw_str):
        if raw_str[i] == '#':
            if i > 0:
                result_string = result_string[:-1]
            i += 1
        else:
            result_string += raw_str[i]
            i += 1
    return result_string
