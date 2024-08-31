# ## RULES:
# > No interner, no help to each other!
# > Send the exam to github
# > You have 2 hours only

# ### 1 Question
# Given a string consisting of words separated by spaces. Determine how many words there are in it. 
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
# # input
#     lorem ipsum dolor
# # output
#     3

# a=input().split()
# print(len(a))

# ### 2 Question
# Given a string containing spaces. Find the longest word in it, print this word and its length. If there are several such words, print the first one.
# Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите  это слово и его длину. Если таких слов несколько, выведите первое из них.
# # input
#     one two three four five six
# # output
#     three
#     5

# a=input().split()
# maxx=0
# cnt=""
# for i in a:
#     if len(i)>maxx:
#         cnt=i
#         maxx=len(i)
# print(f"{cnt}\n{maxx}")

# ### 3 Question
# Print the value of the smallest odd element of the list, and if there are no odd elements in the list, print the number 0.
# Выведите значение наименьшего нечетного элемента списка, а если в списке нет нечетных элементов - выведите число 0.
# # input
#     0 1 2 3 4
# # output
#     1

# lst=list(map(int,input().split()))
# minn=9
# for i in lst:
#     if i%2!=0:
#         if i<minn:
#             minn=i
#     else:
#         minn==0
# print(minn)

# ### 4 Question
# Given a list of numbers. If it contains two adjacent elements of the same sign, print these numbers. If there are no adjacent elements of the same sign, do not output anything. If there are several such pairs of neighbors, print the first pair.
# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей несколько - выведите первую пару.
# # input
#     -1 2 3 -1 -2
# # output
#     2 3

# lst=list(map(int,input().split()))
# for i in range(len(lst)-1):
#     if lst[i]>0 and lst[i]+1>0 or lst[i]<0 and lst[i]+1<0:
#         print(lst[i],lst[i+1])
#         break

# ### 5 Question
# Write a function that removes any non-letters from a string, returning a well-known film title.
# "Напишите функцию, которая удаляет любые не буквенные символы из строки, возвращая известное название фильма."
# # input
#     letters_only("R!=:~0o0./c&}9k`60=y")
# # output
#     "Rocky"

# def delete(a):
#     b=""
#     for i in a:
#         if i.isalpha() or i=="":
#             b+=i
#     return b
# a=input()
# print(delete(a))

# ### 6 Question
# Create a function that finds the word "bomb" in the given string (not case sensitive). If found, return "Duck!!!", otherwise, return "There is no bomb, relax.".
# Создайте функцию, которая находит слово 'bomb' в данной строке (регистр не имеет значения). Если найдено, вернуть 'Duck!!!', иначе вернуть 'There is no bomb, relax.'
# # input                                             #output
#     bomb("Hey, did you think there is a bomb?")    ➞ "Duck!!!"
#     bomb("This goes boom!!!")                      ➞ "There is no bomb, relax."

# def slova(a):
#     if "bomb" in a:
#         return "Duck!!!"
#     else:
#         return "There is no bomb, relax."
# a=input()
# print(slova(a))

# ### 7 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 
# # input                                             #output
# sum_of_vowels("Do I get the correct output?")       10

# def sum(a):
#     vowels={"A":4, "E":3, "I":1, "O":0, "U":0}
#     sum=0
#     for i in a.upper():
#         if i in vowels:
#             sum+=vowels[i]
#     return sum
# a=input()
# print(sum(a))

# ### 8 Question
# A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not. (7 + 5 = 12. 75 is not exactly divisible by 12). Число называется Харшадом, если оно делится ровно на сумму своих цифр. Создайте функцию, которая определяет, является ли число Харшадом или нет. (7 + 5 = 12. 75 не делится на 12 точно). 

# # input             #output
# is_harshad(75)      False

# Input               Output
# is_harshad(481)     True

# def test(a):
#     digit_sum=sum(int(digit) for digit in str(a))
#     return a%digit_sum==0
# a=int(input())
# if test(a):
#     print(a)

# ### 9 Question
# Create a function that takes a string and censors words over four characters with '*'.
# Создайте функцию, которая принимает строку и заменяет слова длиннее четырех символов на '*'.

# # input                             #output
# censor("The code is fourty")        "The code is *****"
# censor("Two plus three is five")    "Two plus ***** is five"

# def test(a):
#     words=a.split()
#     for i in range(len(words)):
#         if len(words[i])>4:
#             words[i]="*"
#     return " ".join(words)
# a=input()
# print(test(a))


# ### 10 Question
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 

# Вам дан массив цен, где цены[i] — цена данной акции на i-й день. Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции и выбрав другой день в будущем для продажи этой акции. Верните максимальную прибыль, которую вы можете получить от этой сделки. Если вы не можете получить прибыль, верните 0.

# Ба шумо массиви нархҳо дода мешавад, ки дар он нархҳо[i] нархи саҳмияҳои додашуда дар рӯзи i мебошанд. Шумо мехоҳед, ки фоидаи худро тавассути интихоби як рӯз барои харидани як саҳмия ва интихоби рӯзи дигар дар оянда барои фурӯши ин саҳмия ба ҳадди аксар расонед. Фоидаи ҳадди аксарро, ки шумо аз ин транзаксия ба даст оварда метавонед, баргардонед. Агар шумо ягон фоида ба даст наоваред, 0-ро баргардонед.

# #### Example 1:
#     Input: prices = [7,1,5,3,6,4]
#     Output: 5
#     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#     Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell. / Покупайте в день 2 (цена = 1) и продавайте в день 5 (цена = 6), прибыль = 6-1 = 5. Обратите внимание, что покупка во второй день и продажа в первый день не разрешены, поскольку вы должны купить, прежде чем продавать.

# #### Example 2:
#     Input: prices = [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transactions are done and the max profit = 0. / В этом случае транзакции не выполняются, а максимальная прибыль = 0.
