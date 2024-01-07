# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути
# кількість видаленних елементів.

# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.

# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
# список також передається як параметр. Функція повертає новий список, який містить отримані результати.


# Завдання 1


# def multiply_elements(numbs):
#     if not numbs:
#         raise ValueError("Список порожній.")
#
#     result = 1
#
#     for num in numbs:
#         result *= num
#
#     return result
#
#
# try:
#     my_list = [1, 2, 3, 4, 5]
#     product_result = multiply_elements(my_list)
#     print(f"Добуток елементів у списку {my_list}: {product_result}")
# except ValueError as e:
#     print(f"Помилка: {e}")


# Завдання 2


# def find_minimum(numbs):
#     if not numbs:
#         raise ValueError("Список порожній.")
#     min_number = min(numbs)
#
#     return min_number
#
#
# try:
#     my_list = [1, 2, 3, 4, 5]
#     min_value = find_minimum(my_list)
#     print(f"Мінімальний елемент у списку {my_list}: {min_value}")
# except ValueError as e:
#     print(f"Помилка: {e}")


# Завдання 3


# import random
#
# numbers = [random.randint(-10, 40) for _ in range(10)]
#
# print(numbers)
#
#
# def is_simple(number: int) -> bool:
#     if number < 2:
#         return False
#
#     for num in range(2, number):
#         if number % num == 0:
#             return False
#
#     return True
#
#
# def get_simple_numbers_from_list(nums: list[int]) -> None:
#     for num in nums:
#         if is_simple(num):
#             print(num, end=" ")
#
#     print()
#
#
# get_simple_numbers_from_list(numbers)

#
# Завдання 4


# def remove_number_from_list(number_to_remove, numbers):
#
#     if not numbers:
#         raise ValueError("Список порожній.")
#
#     try:
#         count_removed = numbers.count(number_to_remove)
#         numbers = [x for x in numbers if x != number_to_remove]
#         return count_removed
#     except Exception as e:
#         raise e
#
#
# try:
#     my_list = [1, 2, 3, 4, 2, 5, 2, 6]
#     number_to_remove = int(input("Введіть число для видалення: "))
#     removed_count = remove_number_from_list(number_to_remove, my_list)
#     print(f"Кількість видалених чисел {number_to_remove} зі списку {my_list}: {removed_count}")
# except ValueError as e:
#     print(f"Помилка: {e}")
# except Exception as e:
#     print(f"Інша помилка: {e}")


# Завдання 5


# def merge_lists(list1, list2):
#
#     if not list1 or not list2:
#         raise ValueError("Один або обидва вхідні списки порожні.")
#
#     try:
#         merged_list = list1 + list2
#         return merged_list
#     except Exception as e:
#         raise e
#
#
# try:
#     list_1 = [1, 2, 3]
#     list_2 = [4, 5, 6]
#     merged_result = merge_lists(list_1, list_2)
#     print(f"Об'єднаний список: {merged_result}")
# except ValueError as e:
#     print(f"Помилка: {e}")
# except Exception as e:
#     print(f"Інша помилка: {e}")


# Завдання 6

# def power_list_elements(power, numbers):
#
#     if not numbers:
#         raise ValueError("Список порожній.")
#
#     try:
#         powered_elements = [num ** power for num in numbers]
#         return powered_elements
#     except Exception as e:
#         raise e
#
#
# try:
#     my_numbers = [1, 2, 3, 4, 5]
#     power_value = 2
#     result_powered_list = power_list_elements(power_value, my_numbers)
#     print(f"Список чисел піднятих до ступеня {power_value}: {result_powered_list}")
# except ValueError as e:
#     print(f"Помилка: {e}")
# except Exception as e:
#     print(f"Інша помилка: {e}")

