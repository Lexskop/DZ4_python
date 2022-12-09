# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def get_encrypt_text(alfabet: str, text: str, key: int) -> str:
    """
    Функция непосредственного шифрования с ключом
    """
    en_text = ''
    alfabet_long = len(alfabet)
    for simbol in text:
        i = 0
        # index = alfabet.find(simbol)
        for s in alfabet:
            if simbol == s:
                index = i + key
            i += 1
        if index > alfabet_long:
            index -= alfabet_long
            # (index+key) % len(alfabet_long)
        en_text += alfabet[index]
    return en_text


def get_decrypt_text(alfabet: str, text: str, key: int) -> str:
    """
    Функция непосредственной дешифровки с ключом
    """
    de_text = ''
    alfabet_long = len(alfabet)
    for simbol in text:
        i = 0
        for s in alfabet:
            if simbol == s:
                index = i - key
            i += 1
        if index < 0:
            index = alfabet_long + index
        if index >= alfabet_long:
            index = index - alfabet_long
        de_text += alfabet[index]
    return de_text

def decr_initialization():
    """
    Функция начала шифрования
    """
    initial_text = input('Введите текст для шифрования -> ')
    key = int(input('Введите ключ зашифровки -> '))
    en_text = get_encrypt_text(alfabet, initial_text, key)
    file_encript = open('encript.txt', 'w', encoding='utf-8')
    file_encript.write(en_text)
    file_encript.close()
    print('Текст зашифрован и находится в файле encript.txt')
    user_wish()

def encr_initialization():
    """
    Функция начала дешифровки
    """
    key = int(input('Введите ключ дешифровки -> '))
    file_encript = open('encript.txt', 'r', encoding='utf-8')
    enc_text = file_encript.read()
    file_encript.close()
    de_text = get_decrypt_text(alfabet, enc_text, key)
    file_decript = open('decript.txt', 'w', encoding='utf-8')
    file_decript.write(de_text)
    file_decript.close()
    print('Текст дешифрован и находится в файле decript.txt')
    user_wish()

def user_wish():
    """
    Метод для возможности не закрывая программу воспользоваться ею еще раз
    """
    user_choice = input(
        'Если вы хотите зашифровать текст - введите 1, если хотите дешифровать текст - введите 2. Для выхода - введите N -> ')
    while user_choice != '1' and user_choice.lower() != 'n' and user_choice != '2':
        user_choice = input(
            'Пожалуйста, введите верное решение. Если вы хотите зашифровать текст - введите 1, если хотите дешифровать текст - введите 2. Для выхода - введите N -> ')
    if user_choice == '1':
        decr_initialization()
    elif user_choice == '2':
        encr_initialization()
    elif user_choice.lower() != 'n':
        print('Bye!')

alfabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя !"№;%:?*()'
user_wish()