# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:
# Внутри декоратора, после вызова функции, проверьте тип результата с помощью
# функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью функции
# print().


def check_is_number(func):
    def wrapper(*args, **kwargs):
        # Проверка числовых аргументов
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Аргументы должны быть числами")
        for v in kwargs.values():
            if not isinstance(v, (int, float)):
                raise ValueError("Аргументы должны быть числами")
        result = func(*args, **kwargs)
        # Проверка результата
        if not isinstance(result, (int, float)):
            print("Ошибка: результат функции не является числом!")
        return result
    return wrapper


def check_is_string(func):
    def wrapper(*args, **kwargs):
        # Проверка строковых аргументов
        for arg in args:
            if not isinstance(arg, str):
                raise ValueError("Аргументы должны быть строкой")
        for v in kwargs.values():
            if not isinstance(v, str):
                raise ValueError("Аргументы должны быть строкой")
        result = func(*args, **kwargs)
        return result
    return wrapper


@check_is_number
def arguments_summary(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


@check_is_string
def concat_str(*args, **kwargs):
    result = ""
    for arg in args:
        result += arg
    for v in kwargs.values():
        result += v
    return result
