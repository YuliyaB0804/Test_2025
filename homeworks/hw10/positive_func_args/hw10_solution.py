# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки, является ли аргумент положительным
# числом.
# Если аргумент не соответствует условию, используйте оператор raise для
# вызова исключения ValueError.


def validate_arguments(func):
    def wrapper(a, b):
        if not (isinstance(a, (int, float)) and a > 0):
            raise ValueError(f"Ошибка: аргумент a={a} не является положительным числом!")
        if not (isinstance(b, (int, float)) and b > 0):
            raise ValueError(f"Ошибка: аргумент b={b} не является положительным числом!")
        return func(a, b)
    return wrapper


@validate_arguments
def sum_positive(a, b):
    return a + b
