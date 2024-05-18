# Задание 2

# в наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

# Задание:
# *написать решения в одну строку
#  1. общее количество чисел
count_numbers = sum([len(i) for i in m])
print(count_numbers)

#  2. посчитать общую сумму чисел
sum_numbers = sum([sum(i) for i in m])
print(sum_numbers)

#  3. посчитать среднее значение
average_numbers = sum_numbers / count_numbers
print(average_numbers)

#  4. собрать все множества в один кортеж
all_sets = tuple([i for i in m])
print(all_sets)
