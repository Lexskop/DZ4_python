# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def search_uniq_elements(elements: list[int]) -> list[int]:
    """
    Выдает список неповторяющихся элементов

    Args:
    list[int] - список чисел
    Returns
    list[int] - список чисел
    """
    new_list = []
    for i in elements:
        if not new_list.count(i):
            new_list.append(i)
        new_list.sort()
    return elements, new_list

print(f'{search_uniq_elements([1,1,1,1,2,2,2,3,3,3,4,9,3,8,1])}')