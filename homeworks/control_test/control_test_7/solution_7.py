some_string = "abcdef...xyz"


def f(s, n):
    part = s[:n]
    return part + part[:-1][::-1]


print(f(some_string, 1))
print(f(some_string, 2))
print(f(some_string, 3))
print(f(some_string, 4))
