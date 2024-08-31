# BASIC OF PYTHON EXAM 1
# Task1: Given two integers A and B (A < B). List all in descending order integers between 
# A and B (not including numbers A and B).
# Input 
# A = 3
# B = 10
# Output
# 9 8 7 6 5 4


# a=int(input())
# b=int(input())
# while b>a+1:
#     b-=1
#     print(b,end=" ")

# ---------------------------------------------------------------------------------------------------------------
# Task2: Write a program in PYTHON to check whether a number is prime or not.
# Input 
# Input a number to check prime or not: 13
# Output
# The entered number is a prime number.

# a=int(input())
# i=1
# cnt=0
# while i<=a:
#     i+=1
#     if a%i==0:
#         cnt+=1

# if cnt>2:
#         print("The entered number is not a prime number.")
# else:
#      print("prime")



# # ----------------------------------------------------------------------------------------------------------------
# Task3: Write a program in PYTHON to find the sum of digits of a given number.
# Input 
# Input a number: 1234
# Output
# The sum of digits of 1234 is: 10

# a=int(input())
# sum=0
# while a>0:
#     last=a%10
#     sum+=last
#     a//=10
# print(sum)

# -----------------------------------------------------------------------------------------------------------------
# Task4: Write a program in PYTHON to calculate the sum of the series (1*1) + (2*2) + 
# (3*3) + (4*4) + (5*5) + ... + (n*n).
# Input 
# Input the value for nth term: 5
# Output
# 1*1 = 1
# 2*2 = 4
# 3*3 = 9
# 4*4 = 16
# 5*5 = 25
# The sum of the above series is: 55

# a=int(input())
# i=0
# sum=0
# while i<=a:
#     i+=1
#     print(f"{i}*{i} = {i*i}")
#     x=i*i
#     sum+=x
#     if i==a: break
# print("The sum of the above series is:",sum)
# ------------------------------------------------------------------------------------------------------------------
# Task5: Write a program in PYTHON to list non-prime numbers from 1 to an upperbound.
# Input 
# Input the upperlimit: 25
# Output
# The non-prime numbers are: 4 6 8 9 10 12 14 15 16 18 20 21 22 24 25

# a=int(input())
# i=0
# while i<=a:
#     i+=1
#     if i%

# -------------------------------------------------------------------------------------------------------------------
# Task6: 4 numbers are entered: a , b , c and d . Print all numbers from a to b that give 
# the remainder c when divided by d . If there are no such numbers, then nothing should be 
# output.
# Input 
# A = 2
# B = 5
# C = 0
# D = 2
# Output
# 2 4
# ----------------------------------------------------------------------------------------------------------------------
# Task7: 2 numbers are entered: x and d . Count and output one number - how many times 
# the digit d appears in the notation of a natural number x.
# Input 
# x = 6323
# d = 3
# Output
# 2
# -----------------------------------------------------------------------------------------------------------------------
# Task8: Enter a natural number x. Print a number consisting of the digits of the given 
# number x in reverse order. Leading zeros are not required.
# Input 
# x = 1234
# Output
# ReverseX = 4321
# ----------------------------------------------------------------------------------------------------------------------
# Task9: Write a program in PYTHON to display the n terms of odd natural number and 
# their sum.
# Input 
# Input number of terms: 5
# Output
# The odd numbers are: 1 3 5 7 9
# The Sum of odd Natural Numbers upto 5 terms: 25
# ----------------------------------------------------------------------------------------------------------------------
# Task10: Write a program in PYTHON to find the number and sum of all integer between n 
# and m which are divisible by 9.
# Input 
# n = 100
# m = 200
# Output
# Numbers between 100 and 200, divisible by 9:
# 108 117 126 135 144 153 162 171 180 189 198
# The sum : 1683