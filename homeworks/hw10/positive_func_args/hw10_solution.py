# Положительные аргументы функции
#
# Напишите декоратор @validate_arguments, который проверяет, что все аргументы
# функции являются положительными числами. Если встречается аргумент, не
# соответствующий этому условию, функция должна вывести сообщение об ошибке.
# Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки, является ли аргумент положительным
# числом.
# Если аргумент не соответствует условию, используйте оператор raise для
# вызова исключения ValueError.


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args):
            if not (isinstance(arg, (int, float)) and arg > 0):
                raise ValueError(f"Argument at position {index} ({arg}) is not"
                                 f" a positive number")
        for key, value in kwargs.items():
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError(f"Argument '{key}' ({value}) is not "
                                 f"a positive number")
        return func(*args, **kwargs)
    return wrapper


# Пример функции с декоратором: суммирует положительные числа
@validate_arguments
def sum_positive(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
