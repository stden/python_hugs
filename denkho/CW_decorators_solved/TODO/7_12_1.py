# Вводится строка целых чисел через пробел.
# Напишите функцию mysum, которая преобразовывает эту строку в список чисел и возвращает их сумму.
#
# Определите декоратор nice для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции mysum:
#
# Sample Input:
#
# 5 6 3 6 -4 6 -1
# Sample Output:
#
# 26

# ===================== ваш код =====================





# ===================== проверка =====================
assert nice, "декоратор не найден"
str_1 = "5 6 3 6 -4 6 -1"
res = mysum(str_1)
assert res == 26, "функция mysum вернула неожиданный результат"
print(res)
