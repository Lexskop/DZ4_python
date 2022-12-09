# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def give_number(input_str: str) -> int:
    """
    Ввод числа
    """
    while True:
        try:
            num = int(input(input_str))
            return num
        except ValueError:
            print('Вы ввели не число')

def get_multiplier_list(num: int) -> list:
    """
    Принимает введенное число. Покажет список простых множителей этого числа

    Args:
        int - целое число
    Returns:
        list - список простых множителей введенного числа
    """
    mult = []
    for i in range(2,num+1):
        while not num % i:
            if not mult.count(i):
                mult.append(i)
            num //= i
        i +=1
    return mult

num = give_number('Введите число: ')
multiplier = get_multiplier_list(num)
print(f'Простые множители числа {num} -> {multiplier}')
