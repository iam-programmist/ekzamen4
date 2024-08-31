# Exam 1
# Task1: One combine threshed A tons of grain, and the second harvested B tons less. How many tons of 
# grain did both combiners thresh?
# Input 
# A = 34
# B = 10
# Output
# 58

a=int(input())
b=int(input())
b=a-b
print(a+b)


# Task2. Write a program in PYTHON to display the next and previous even number of the given number.
# Input 
# The number is : 150
# Output
# The next number for the number 150 is 152
# The previous number for the number 150 is 148

# a=int(input())
# if a%2==0:
#     print(f"The next number for the number {a} is {a+2}")
#     print(f"The previous number for the number {a} is {a-2}")
# else:
#     print(f"The next number for the number {a} is {a+1}")
#     print(f"The previous number for the number {a} is {a-1}")

# Task3: There were A passengers on the bus. B passengers got off at the bus stop and C entered. How 
# many passengers were on the bus?
# Input 
# A = 53
# B = 12
# C = 18
# Output
# 59

# a=int(input())
# b=int(input())
# c=int(input())
# print((a-b)+c)

# Task4. Given a five digit number. Find the sum and product of its digits.
# Input 
# 19283
# Output
# The sum of the digits is : 1+9+2+8+3 = 23 
# The product of the digits is : 1*9*2*8*3 = 432 

# a=int(input())
# sum=0
# zarb=1
# while a>0:
#     last=a%10
#     sum+=last
#     zarb*=last
#     a//=10
# print(f"The sum of the digits is : {sum}")
# print(f"The product of the digits is : {zarb}")

# Task5: Given a four digit number. Find the maximum number from its digits.
# Input 
# The number is: 1502
# Output
# Max = 5

# maxx=0
# a=int(input())
# while a>0:
#     last=a%10
#     if last>maxx:
#         maxx=last
#     a//=10
# print(f"Max = {maxx}")

# Task6: Four integers are given. Find the number of positive, negative and the number of zeros in the 
# original set. Input and output should be the same as shown in example below.
# Input 
# number1: 2
# number2: 3
# number3: -3
# number4: 0
# Output
# Number of positive: 2
# Number of negative: 1
# Number of zeros: 1

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# pos=0
# neg=0
# zero=0

# if a>0: pos+=1
# if b>0: pos+=1
# if c>0: pos+=1
# if d>0: pos+=1

# if a<0: neg+=1
# if b<0: neg+=1
# if c<0: neg+=1
# if d<0: neg+=1

# if a==0: zero+=1
# if b==0: zero+=1
# if c==0: zero+=1
# if d==0: zero+=1
# print(f"Number of positive: {pos}")
# print(f"Number of negative: {neg}")
# print(f"Number of zeroes: {zero}")

# Task7: Write a program in PYTHON to display n terms of natural number and their sum.
# Input 
# Input a number of terms: 7
# Output
# The natural numbers upto 7th terms are: 1 2 3 4 5 6 7
# The sum of the natural numbers is: 28

# a=int(input())
# i=0
# sum=0
# while i<=a:
#     sum+=i
#     i+=1
#     print("The natural numbers upto th terms are: ",i-1,end=" ""\n")
# print(f"The sum of the natural numbers is: {sum}")

# Task8: Given a real number — the price of 1 kg of sweets. Output cost 1,2, . . . , 10 kg of sweets.
# Input 
# Coast: 5.50
# Output
# 1 kg – 5.5
# 2 kg – 11
# 3 kg – 16.5
# 4 kg – 22
# 5 kg – 27.5
# 6 kg – 33
# 7 kg – 38.5
# 8 kg – 44
# 9 kg – 49.5
# 10 kg – 55
# 11 kg – 60.5
# 12 kg - 66

# a=float(input())
# i=0
# zarb=1
# while i<=12:
#     i+=1
#     zarb*=i
#     print(f"{1} kg - {zarb}")
#     print(f"{2} kg - {zarb}")
#     print(f"{3} kg - {zarb}")
#     print(f"{4} kg - {zarb}")
#     print(f"{5} kg - {zarb}")
#     print(f"{6} kg - {zarb}")
#     print(f"{7} kg - {zarb}")
#     print(f"{8} kg - {zarb}")
#     print(f"{9} kg - {zarb}")
#     print(f"{10} kg - {zarb}")
#     print(f"{11} kg - {zarb}")
#     print(f"{12} kg - {zarb}")

# Task9: Write a program in PYTHON to find the factorial of a number.
# Input 
# Input a number to find the factorial: 5
# Output
# The factorial of the given number is: 120

# a=int(input())
# i=0
# sum=0
# zarb=1
# while i<=a:
#     i+=1
#     zarb*=i
#     # sum+=zarb
# print(zarb)

# Task10: Write a program in PYTHON to display the pattern like right angle triangle with number.
# Input 
# Input number of rows: 5
# Output
# 1
# 12
# 123
# 1234
# 12345

# a=int(input())
# i = 1
# while i <= a:
#     j = 1
#     while j <= i:
#         print(j,end="")
#         j += 1
#     print()
#     i += 1