# #1

# def a(grams):
#     print("ounces =", 28.3495231 * grams)
# a(int(input()))  

# #2

# def a(F):
#     print("C =",(5 / 9) * (F-32))
# a(int(input())) 

# #3

# def solve(numheads, numlegs):
#     R=(numlegs-2*numheads)/2
#     C=35-R
#     print("Rabbits:",int(R),"Chickens:",int(C))

# solve(35,94)    

# #4
# import math
# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
# def filter_prime(list):
#     print([num for num in list if prime(num) == True])

# numbers = list(map(int, input().split()))
# filter_prime(numbers)

# #5
# def perm(s, ans):
#     if len(s) == 0:
#         print(ans)
#         return
#     for i in range(len(s)):
#         a = s[i]
#         left = s[:i]
#         right = s[i+1 :]
#         rest = left + right
#         perm(rest, ans + s[i])

# word = str(input())
# perm(word, '')

#6

# def reverse(sentence):
#     i = len(sentence)-1
#     while i>=0:
#         print(sentence[i], end=' ')
#         i-=1
# sentence = list(map(str, input().split()))
# reverse(sentence)

# #7

# def three_after_three(numbers):
#     i = 0
#     while i < len(numbers) - 1 :
#         if numbers[i] == 3 and numbers[i+1] ==3 :
#             return True
#             break
#         i+=1
#     return False
# array = list(map(int, input().split()))
# print(three_after_three(array))

# #8

# def spy_game(nums):
#     for i in range(len(nums)-2):
#         if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
#             return True
#     return False
# nums = list(map(int, input().split()))
# print(spy_game(nums))

# #9

# def volume(radius):
#     return float(((4*3.14)/3) * (radius**3))
# radius=float(input())
# print(f'Volume of the sphere with radius {radius} is {volume(radius)} unit cube')

# #10

# def unique(list):
#     new_list=[]
#     for i in list:
#         if i in new_list:
#             pass
#         else:
#             new_list.append(i)
#     return new_list
# list = list(map(int, input().split()))
# print(unique(list))

# #11

# def palindrome(string):
#     return string == string[::-1]
# string = str(input())
# print(palindrome(string))

# #12

# def histogram(list):
#     for i in range(len(list)):
#         print('*'*list[i], end='\n')
# list = list(map(int, input().split()))
# histogram(list)

# #13
# import random

# print("Hello! What is your name?")
# name = input()

# secret_number = random.randint(1, 20)  
# print(f"Well, {name}, I am thinking of a number between 1 and 20.")

# attempts = 0

# while True:
#     print("Take a guess.")
#     guess = int(input())
#     attempts += 1

#     if guess < secret_number:
#         print("Your guess is too low.")
#     elif guess > secret_number:
#         print("Your guess is too high.")
#     else:
#         print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#         break  

 