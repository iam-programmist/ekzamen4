# ## RULES:
# > No interner, no help to each other!
# > Send the exam to github
# > You have 2 hours only


# ### 1 Question
# At Softclub students only pass to the next month if the average of four exams is equal to or more than 80. Students want to create a program to show whether they passed the exam or not. They want you to Help them to create this kind of program.
# Program should display the text “Your average is average”, and text  “You have successfully passed the exam. Happy coding” if the average is more than 80, otherwise display text “You have failed the exam. Study hard!”

# В Softclub студенты переходят на следующий месяц только в том случае, если средний балл по четырем экзаменам равен или больше 80. Студенты хотят создать программу, которая покажет, сдали они экзамен или нет. Они хотят, чтобы вы помогли им создать такую ​​программу. Программа должна отображать текст «Your average is {average}» и текст «You have successfully passed the exam. Happy coding», если средний балл больше 80, в противном случае отображать текст «You have failed the exam. Study hard!»
# # input
#     exam1: 80
#     exam2: 80
#     exam3: 80
#     exam4: 81
# # output
#     Your average is 80.25
#     You have successfully passed the exam. Happy coding 

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# sum=(a+b+c+d)/4
# if sum>=80:
#     print(f"Your average is {sum}")
# else:
#     print("You have successfully passed the exam. Happy coding")

# ### 2 Question
# Given a positive integer N. Print N in reverse order with a space between.
# Дано положительное целое число N. Выведите N в обратном порядке, разделив их пробелом.
# # input
#     N = 13324
# # output
#     4  2  3  3  1

# a=int(input())
# while a>0:
#     last=a%10
#     print(last,end=" ")
#     a//=10

# ### 3 Question
# Given a list of numbers and the index of the element in the list k. Remove an element with index k from the list by shifting to the left all elements to the right of the element with index k.
# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
# # input
#     7 6 5 4 3 2 1
#     2
# # output
#     7 6 4 3 2 1

# lst=list(map(int,input().split()))
# a=len(lst)-1
# b=int(input())
# i=b
# if b<a:
#     while i<a:
#         i+=1
#         lst.pop()
# print(*lst)


# ### 4 Question
# A sequence of integers ending with the number 0 is entered (the number 0 itself is not included in the sequence). Determine the number of positive and negative elements of the sequence.
# Введена последовательность целых чисел, заканчивающаяся цифрой 0 (сама цифра 0 в последовательность не входит). Определите количество положительных и отрицательных элементов последовательности.
# # input
#     1
#     1
#     -7
#     9
#     0
# # output
#     positive: 3
#     negative: 1

# pos=0
# neg=0
# while True:
#     a=int(input())
#     if a==0: break
#     if a>0: pos+=1
#     if a<0: neg+=1
# print(f"positive: {pos}")
# print(f"negative: {neg}")

# ### 5 Question
# Calculate the sum of a sequence of natural numbers. The sequence stops when the user enters two zeros in a row.
# Вычислить сумму последовательности натуральных чисел. Последовательность останавливается, когда пользователь вводит два нуля подряд.
# # input
#     1
#     0
#     7
#     0
#     9
#     0
#     0
# # output
#     17

# sum=0
# zero=-1
# while True:
#     a=int(input())
#     if a==0:
#         if zero==0:
#             break
#     sum+=a
#     zero=a
# print(sum)

# ### 6 Question
# Given a string containing spaces. Find the shortest word in it, print this word and its length. If there are several such words, print the first one.
# Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите  это слово и его длину. Если таких слов несколько, выведите первое из них.
# # input
#     one two three four five six
# # output
#     one
#     3

# lst=input().split()
# a=len(lst)
# slova=lst[0]
# dlina=len(slova)
# for i in lst:
#     if len(i)<dlina:
#         slova=i
#         dlina=len(i)
# print(slova)
# print(dlina)

# ### 7 Question
# Print the value of the smallest odd element of the list, and if there are no odd elements in the list, print the number 0.
# Выведите значение наименьшего нечетного элемента списка, а если в списке нет нечетных элементов - выведите число 0.
# # input
#     0 1 2 3 4
# # output
#     1

# lst=list(map(int,input().split()))
# a=len(lst)
# minn=1
# for i in lst:
#     if i%2!=0:
#         if i<=minn:
#             minn=i
# print(minn)

# ### 8 Question
# A list is given. Print those elements that appear in the list only once. Elements must be displayed in the order in which they appear in the list.
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# # input
#     1 2 2 3 3 3
# # output
#     1

# lst=list(map(int,input().split()))
# lst1=[]
# for i in range(len(lst)):
#     cnt=0
#     for j in range(len(lst)):
#         if lst[i]==lst[j]:
#             cnt+=1
#     if cnt==1:
#         lst1.append(lst[i])
# for k in lst1:
#     print(k,end=" ")


# ### 9 Question
# Given a list, ordered in non-decreasing order of the elements in it. Determine how many different elements it contains.
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
# # input
#     1 2 2 3 3 3
# # output
#     3

# lst=list(map(int,input().split()))
# cnt=0
# if len(lst)>0:
#     a=lst[0]
#     cnt=1
#     for i in range(1,len(lst)):
#         if lst[i]!=a:
#             cnt+=1
#             a=lst[i]
# print(cnt)


# ### 10 Question
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Учитывая массив временных интервалов совещаний, состоящий из времени начала и окончания [[s1,e1],[s2,e2],...] (si < ei), найдите минимальное необходимое количество конференц-залов.

# Бо назардошти як қатор фосилаҳои вақти вохӯрӣ, ки аз вақти оғоз ва анҷоми он [[s1,e1],[s2,e2],...] (si < ei) иборат аст, шумораи ҳадди ақали утоқҳои конфронси лозимиро пайдо кунед.

# #### Example 1:
#     Input: intervals = [(0,30),(5,10),(15,20)]
#     Output: 2
#     Explanation:
#     We need two meeting rooms / Нам нужны два конференц-зала
#     room1: (0,30)
#     room2: (5,10),(15,20)

# #### Example 2:
#     Input: intervals = [(2,7)]
#     Output: 1
#     Explanation:
#     Only need one meeting room / Нужен только один конференц-зал

