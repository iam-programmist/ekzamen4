# ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.

# Методҳои модули datetime: date,time,timedelta,day,month,week,year
# Методҳои модули randome: randint,randrange,shufle,choise,choises

# ### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.

# open-барои кушодани файл,
# close-барои махкам кардани фвйл
# with open-барои хам кушодан ва махкам кардан
# read-барои хондани файл
# write-барои ягончи навистан дар файл

# ### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.

# Github-ин портал барои програмистон аст,ки дар ончо мо метавонем коди навистагиамонро аз локални репозитори ба удалёни репазитори партоем

# ### 1 Question
# Write a Python program to insert an element at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]
# # input
#     Enter an element: Sorbon
#     Index: 3
# # output
#     [1, 1, 2, "Sorbon", 3, 4, 4, 5, 1]

# my_list = [1, 1, 2, 3, 4, 4, 5, 1]
# a = input()
# b = int(input())
# my_list.insert(b, a)
# print(my_list)

# ### 2 Question
# Write program to print 2 days before, today, 2 days after / Напишите программу для печати позавчера, сегодня, послезавтра. / Барномаи нависед, то пареррӯз, имрӯз, фардои дигарро чоп кунад 

# from datetime import datetime, timedelta
# today = datetime.now()
# yesterday = today - timedelta(days=2)
# tomorrow = today + timedelta(days=2)
# print(yesterday.strftime("%Y-%m-%d"))
# print(today.strftime("%Y-%m-%d"))
# print(tomorrow.strftime("%Y-%m-%d"))

# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.
# Input: 17.02.2024           Output: 12.02.2024

# from datetime import datetime, timedelta
# today = datetime.now()
# res = today - timedelta(days=5)
# print(today.strftime("%Y-%m-%d"))
# print(res.strftime("%Y-%m-%d"))

# ### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 
# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10

# vowels = {
#     'A': 4,
#     'E': 3,
#     'I': 1,
#     'O': 0,
#     'U': 0
# }
# a = input()
# sum = 0
# a = a.upper()
# for i in a:
#     if i in vowels:
#         sum += vowels[i]
# print(sum)

# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# input
#     3
# otput
#     Tajikistan

# with open('my_file.txt', 'a+') as file:
#     lines = file.write("Hello World\nHello\nHi")
#     n = int(input())
#     print(lines[n - 1].strip())

# ### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 

# a = input()
# with open("test.txt", "a+") as file:
#     lines = file.readlines("Hello World\nHello\nHi")
# for i in range(len(lines)):
#     if (i + 1) % 2 != 0:
#         lines[i] = a + '\n'
# with open("test.txt", "a+") as file:
#     file.writelines(lines)
# print(a)

# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5

# import random
# a = int(input())
# big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# small = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
# all = big + small + digits + symbols
# res = ''.join(random.choice(all) for i in range(a))
# print(res)

# ### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# a = int(input())
# dict1 = {}
# for i in range(1, a + 1):
#     dict1[i] = i ** 2
# print(dict1)

# ### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical. Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.
# Input       
# char_appears("She sells sea shells by the seashore.", "s")
# Output
# [1, 2, 1, 2, 0, 0, 2]

# a = input()
# b = input()
# c = b.lower()
# words = a.split()
# cnt = {}
# for word in words:
#     lower_word = word.lower()
#     count = lower_word.count(c)
#     cnt[word] = count
# print(cnt)

# ### 10 Task
# Given a list of elements of any data types. Create a Python program to separate elements by their types and save them into a new dictionary.
# The keys of a dictionary must be of a data type, and its element must be data belonging to that type.
# Дан список элементов любых типов данных. Создайте программу Python для разделения элементов по их типам и сохранения их в новый словарь.
# Ключи словаря должны иметь тип данных, а его элементом должны быть данные, принадлежащие этому типу.
# # input
#     1 hello True 12 Muhammad
# # output
#     {"int": [1,12], "str": ["hello", "Muhammad"], "bool": [True]}
