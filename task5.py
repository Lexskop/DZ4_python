# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

def write_to_file_task_5(string = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'):
    """
    Начальные данные для записи в файл
    """
    with open ('file_task_5.txt','w') as file:
        file.write(string)
write_to_file_task_5()

def convert_to_RLE_alg() -> str:
    """
    Функция сжатия файла
    """
    with open('file_task_5.txt','r') as file:
        text_for_compress = file.read()
    index = 0
    count = 1
    compr_text = ''
    text_for_compress += ' '
    while index < len(text_for_compress)-1:
        if text_for_compress[index].isdigit():
            compr_text+=text_for_compress[index]
        elif text_for_compress[index] == text_for_compress[index+1]:
            count+=1
        elif text_for_compress[index] != text_for_compress[index+1]:
            if count == 1:
                compr_text+=text_for_compress[index]
            else:
                compr_text+= str(count) + text_for_compress[index]
            count = 1
        index +=1
    with open('file_task_5_compr','w') as file:
        file.write(compr_text)
    return compr_text

print(f'Сжатый текст: {convert_to_RLE_alg()}')
compr_text = convert_to_RLE_alg()

def recompression_RLE_to_text() -> str:
    """
    Функция восстановления файла
    """
    with open('file_task_5_compr','r') as file:
        text_from_file = file.read()
    index = 0
    count = ''
    compr_text = ''
    while index < len(text_from_file):
        if text_from_file[index].isdigit():
            count+=text_from_file[index]
        elif count == '':
            compr_text+=text_from_file[index]
        else:
            compr_text+=text_from_file[index]*int(count)
            count = ''
        index +=1
    with open('file_task_5_recompr','w') as file:
        file.write(compr_text)
    return compr_text

print(f'Восстановленный текст: {recompression_RLE_to_text()}')