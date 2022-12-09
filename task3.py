# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def change_letters(spisok: list[str], accept: str) -> str:
    """
    Функция перевода текста с оценкой 5 в верхний регистр
    """
    file_words = ''
    for name in spisok:
        if name.count(accept):
            name = name.upper()
        string = name + '\n'
        file_words += string
    return file_words

file_words = open('file.txt', 'r', encoding='utf-8')
lines_words = file_words.read().split('\n')
file_words.close()

words_new = change_letters(lines_words, accept='5')

file_words = open('file.txt', 'w', encoding='utf-8')
file_words.write(words_new)
file_words.close()