def file_functions(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    information = file.read()
    file.close()

    strings = information.splitlines()
    number_strings = len(strings)
    words = information.split()
    number_words = len(words)
    number_letters = 0
    for character in information:
        if character.isalpha():
            number_letters += 1

    result = (f"\nКоличество строк: {number_strings}\n"
              f"Количество слов: {number_words}\n"
              f"Количество букв: {number_letters}\n")

    file = open(file_name, 'a', encoding='utf-8')
    file.write(result)
    file.close()

    print(result)
