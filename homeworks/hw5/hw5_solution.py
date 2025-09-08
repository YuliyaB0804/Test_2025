# 1. Напишите программу, которая добавляет ‘ing’ к словам
def add_ing(s: str) -> str:
    s += "ing"
    return s


# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
def change_symbol(s: str) -> str:
    return s.replace('#', '/')


# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
def change_order(s: str) -> str:
    word1, word2 = s.split()
    return f"{word2} {word1}"


# 4. Напишите программу, которая удаляет пробел в начале, в конце строки
def clean_string(s: str) -> str:
    return s.strip()


# 5. Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению "pARiS" >> "Paris"
def to_capitalize(s: str) -> str:
    return s.capitalize()


# 6. Перевести строку в список "Robin Singh" => ["Robin", "Singh"],
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
def to_list(s: str) -> list:
    return s.split()


# 7. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
def formatting(array: list, s1: str, s2: str) -> str:
    names = " ".join(array)
    return f"Hello, {names}! {s1} to {s2}"


# 8. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
def to_string(array: list) -> str:
    return " ".join(array)


# 9. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array
def list_to_string(array: list) -> str:
    return ' '.join(array)


# 10. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
def delete_from_list(array: list, indx: int) -> list:
    array.pop(indx)
    return array
