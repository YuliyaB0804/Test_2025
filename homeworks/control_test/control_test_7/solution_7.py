STR1 = "abcdef...xyz"


def f(s, n):
    part = s[:n]
    return part + part[:-1][::-1]


print(f(STR1, 1))
print(f(STR1, 2))
print(f(STR1, 3))
print(f(STR1, 4))
