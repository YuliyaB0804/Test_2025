# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:
# Внутри декоратора, после вызова функции, проверьте тип результата с помощью
# функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью функции
# print().


def check_positive(func):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise ValueError("Аргументы должны быть числами")
            if arg < 1:
                raise ValueError(f"Аргумент в позиции {index} ({arg}) не "
                                 f"является положительным числом")
        for name, v in kwargs.items():
            if not isinstance(v, (int, float)):
                raise ValueError("Аргументы должны быть числами")
            if v < 1:
                raise ValueError(f"Аргумент '{name}' ({v}) не является"
                                 f" положительным числом")
        return func(*args, **kwargs)
    return wrapper


@check_positive
def arguments_summary(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


@check_positive
def arguments_concatenate_negative(*args, **kwargs):
    return sum(args) + sum(kwargs.values())







# Декоратор, который проверяет результат функции
def check_number_output(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float, complex)):
            print("Arguments should be a number")
        return result
    return wrapper

# Пример функции arguments_summary
@check_number_output
def arguments_summary(*args, **kwargs):
    # Ваша логика для суммы аргументов
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total += value
    return total

# Пример функции concat_str
@check_number_output
def concat_str(*args, **kwargs):
    # Ваша логика для конкатенации строк
    result = ''
    for arg in args:
        if not isinstance(arg, str):
            return "Arguments should be a number"
        result += arg
    for value in kwargs.values():
        if not isinstance(value, str):
            return "Arguments should be a number"
        result += value
    return result