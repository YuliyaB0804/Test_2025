s = "abcdef...xyz"


def f(s, n):
    part = s[:n]
    return part + part[:-1][::-1]


print(f(s, 1))
print(f(s, 2))
print(f(s, 3))
print(f(s, 4))
