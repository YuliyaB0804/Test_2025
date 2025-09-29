# Декоратор типов
# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:

# @typed(type=str)
# def add(a, b):
#     return a + b

# add("3", 5) -> "35"
# add(5, 5) -> "55"
# add('a', 'b') -> 'ab’


# @typed(type=float)
# def add(a, b, с):
#     return a + b + с

# add(0.1, 0.2, 0.4) -> 0.7000000000000001


# @typed(type=int)
# def add(a, b, с):
#     return a + b + с

# add(5, 6, 7) -> 18


def typed(arg_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            converted_args = [arg_type(arg) for arg in args]
            converted_kwargs = {key: arg_type(value) for key, value in kwargs.items()}
            result = func(*converted_args, **converted_kwargs)
            return result
        return wrapper
    return decorator


@typed(arg_type=str)
def add_str(a, b):
    return a + b


@typed(arg_type=float)
def add_float(a, b, c):
    return a + b + c


@typed(arg_type=int)
def add_int(a, b, c):
    return a + b + c
