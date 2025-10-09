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
        for name, k in kwargs.items():
            if not isinstance(k, (int, float)):
                raise ValueError("Аргументы должны быть числами")
            if k < 1:
                raise ValueError(f"Аргумент '{name}' ({k}) не является"
                                 f" положительным числом")
        return func(*args, **kwargs)
    return wrapper


@check_positive
def arguments_summary(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


@check_positive
def arguments_concatenate_negative(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
