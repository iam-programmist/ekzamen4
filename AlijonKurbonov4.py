# ## RULES:
# > No interner, no help to each other!
# > Send the exam to github
# > You have 2 hours only

# ### 1 Question
# Дар бораи рекурсия нависед. 

# Рекурсия ин методе мебошад ки функсия худаш худашро фарёд мекунад яъне ба монанди цикл истифода мешавад

# ### 2 Question
# Closure(Замыкания) - ро бо мисолҳо фаҳмонед.

# Замикание ин методе мебошад ки хатто функсия баъди корашро тамом кардан переменнияро дар хотираш мегирад барои далнейшим истифода бурдан

# ### 3 Question
# Контейнерҳоро ба хотир оварда онҳоро нависед. 

# list,tuple,dictionary,set,array

# ### 4 Question
# Дар бораи list, dict comprehension ва args,kwargs нависед.

# list як контейнере мебошад ки аз коллекцияи элементхо иборат мебошад ва индексу элеменет дорад,
# dictionary хам контейнер буда key ва value дорад, key ба маънои индекс value ба маънои эелемент, значение
# comprehension мо метавонем дар даруни он типи элементро алиш кунем ва цикл сардихем боз метавонем бо if кор кунем

# ### 5 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.

# Модулхои datetime : datetime, date, time, datetimenow, hour, day, week, month, year
# Модулхои random : random, randint, randrange, choice, choices

# ### 1 Task
# Write a Python program that converts currency from one denomination to another.
# Создайте программу, которая конвертирует валюту одного номинала в другой.
# # input
#     Enter the amount in TJS: 1
# # output
#     Rub -> 8.33
#     USD -> 0.094
#     EUR -> 0.084
#     UZ_SUM -> 1000

# test = {
#     'USD': 0.094,
#     'EUR': 0.084,
#     'RUB': 8.33,
#     'UZ_SUM': 1000
# }
# a = float(input())
# b = input()
# if b == 'USD' or b == 'EUR' or b == 'RUB' or b == 'UZ_SUM':
#     c = a // test[b]
#     res = c * test
#     print(res)

# ### 2 Task
# Write a Python program to convert a list of multiple integers into a single integer.
# Напишите программу на Python для преобразования списка из нескольких целых чисел в одно целое число.
# # input
#     Sample list: [11, 33, 50]
# # output
#     Expected Output: 113350

# lst = list(map(int,input().split()))
# a = ""
# for i in lst:
#     a += str(i)
# res = int(a)
# print(res)

# ### 3 Task
# Create a closure that concatenates a given string with another string.
# Создайте замыкание, которое объединяет заданную строку с другой строкой.

# # input
#     Tajikistan
# # otput
#     Salom Tajikistan

# def test(a):
#     def test1(b):
#         return a + b
#     return test1
# b = input()
# c = test(b)
# res = c(input())
# print(res)

# ### 4 Task
# Write a recursive function to find the minimum element in a list.
# Напишите рекурсивную функцию для поиска минимального элемента в списке.

# # input
#     2 3 54 2 4 0 5 3 2 54
# # output
#     0

# def test(a, cnt=0):
#     if cnt == len(a) - 1:
#         return a[cnt]
#     minn = test(a, cnt + 1)    
#     return min(a[cnt], minn)
# lst = list(map(int,input().split()))
# res = test(lst)
# print(res)

# ### 5 Task
# Given a natural number n, compute the sum 1^2+2^2+...+n^2.
# Create a function that takes single natural number n. You need to withdraw the calculated amount. Don’t forget to return the result. Solve this problem using the recursion function.

# Дано натуральное число n, вычислите сумму 1^2+2^2+...+n^2.
# Создайте функцию, которая принимает одно натуральное число n. Вам нужно вывести вычисленную сумму. Не забудьте вернуть результат. Решите эту задачу с помощью функции рекурсии.

# input
#     n = 2
# output
#     Expected Output: 5

# def test(n):
#     if n == 1:
#         return 1
#     else:
#         return n + test(n - 1)
# n = int(input())
# res = test(n)
# print(res)

# ### 6 Task
# Given a natural number N, find the sum of the numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions should be proportional to N.
# По данному натуральному числу N найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# # input
#     1
# # output
#     2

# n = int(input())
# sum = 0
# fact = 1
# for i in range(n + 1):
#     if i > 0:
#         fact *= i
#     sum += 1 / fact
# print(sum)

# ### 7 Task
# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# Напишите программу на Python, заменяющую каждый символ слова длиной пять и более символом решетки (#).
# # input
#     Count the lowercase letters in the said list of words:
# # output
#     ##### the ######### ####### in the said list of ######

# a = input()
# words = a.split()
# res = ""
# for i in words:
#     if len(i) >= 5:
#         res += '#' * len(i) + ' '
#     else:
#         res += i + ' '
# if res:
#     res = res[:-1]
# print(res)

# ### 8 Task
# Given a natural number N, find the sum of numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions must be proportional to N.
# Create a function that takes a single number N. It is necessary to display the result of the calculation as a real number with an accuracy of 5 decimal places. Don’t forget to return the result.

# Дано натуральное число N, найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# Создайте функцию, которая принимает одно число N. Необходимо вывести результат вычисления в виде действительного числа с точностью до 5 знаков после запятой. Не забудьте вернуть результат.

# # input
#     N = 1
# # output
#     res = 2

# def test(a):
#     result = a ** 2
#     result_str = str(result)    
#     if '.' in result_str:
#         cnt = result_str.index('.')
#         if len(result_str) - cnt - 1 < 5:
#             result_str += '0' * (5 - (len(result_str) - cnt - 1))
#         result_str = result_str[:cnt + 6]
#     res = float(result_str)
#     print(res)    
#     return res
# a = float(input())
# result = test(a)

# ### 9 Task
# Write a Python program for binary search of an ordered list.
# Напишите программу на Python для двоичного поиска в упорядоченном списке.
# # Example
#     Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
#     Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False


# ### 10 Task
# Given a string containing only English letters (upper and lower case). Add opening and closing brackets as follows: "example" -> "e(x(a(m)p)l)e" (Opening brackets are added before the middle, closing brackets are added after the middle. If the string length is even, there should be 2 symbols in the brackets located in the middle. ("card -> c(ar)d", but not "c(a()r)d"). Solve this problem using the recursion function.

# Дана строка, содержащая только английские буквы (большие и маленькие). Добавить открывающиеся и закрывающиеся скобки по следующему образцу: "example" -> "e(x(a(m)p)l)e" (До середины добавлены открывающиеся скобки, после середины – закрывающиеся. В случае, когда длина строки четна в скобках, расположенных в середине, должно быть 2 символа. ("card -> c(ar)d", но не "c(a()r)d"). Решите эту задачу с помощью функции рекурсии.

# # input                           # input
#     hello                           khayriddin
# # output                          # output
#     h(e(l)l)o                       k(h(a(y(ri)d)d)i)n



