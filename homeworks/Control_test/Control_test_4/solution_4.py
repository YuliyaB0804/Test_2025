def add_one(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
        number += 1
    result = []
    while number > 0:
        result.insert(0, number % 10)
        number //= 10
    return result


number1 = [1, 2, 3]
print(add_one(number1))
