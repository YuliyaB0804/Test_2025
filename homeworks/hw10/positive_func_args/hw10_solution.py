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
        for arg in args:
            if not (isinstance(arg, (int, float)) and arg > 0):
                raise ValueError("Все аргументы должны быть положительными числами.")
        for key, value in kwargs.items():
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError("Все аргументы должны быть положительными числами.")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def sum_positive(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

