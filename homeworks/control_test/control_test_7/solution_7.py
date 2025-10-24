string1 = "abcdef...xyz"


def f(s, n):
    part = s[:n]
    return part + part[:-1][::-1]


print(f(string1, 1))
print(f(string1, 2))
print(f(string1, 3))
print(f(string1, 4))
