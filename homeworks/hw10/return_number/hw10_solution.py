# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:
# Внутри декоратора, после вызова функции, проверьте тип результата с помощью
# функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью функции
# print().


def check_is_number(func):
    def wrapper(a, b):
        result = func(a, b)
        if not isinstance(result, (int, float)):
            print("Ошибка: результат функции не является числом!")
        return result
    return wrapper


@check_is_number
def concat_str(a, b):
    return a + b


@check_is_number
def arguments_summary(a, b):
    return a + b
