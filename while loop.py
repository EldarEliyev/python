#While Loops-
#A.Write a program that asks user for a number between 100 and 500.The program should ask the user until he/she enters the number within a given range.
# user_num = int(input("Enter your number:"))
# total = 0
# while user_num <=500:
#     print(user_num)
#     user_num +=1


# B.Write a program that prints even and odd numbers between 1 to the entered number.
# arr = [20,33, 10, 22, 15, 34]
# n = 0
# while(n< len(arr)):
#     if (arr[n] %2) != 0:
#         print("Number is odd", arr[n])
#         n+=1
#     else:
#         print("Number is Even", arr[n])
#         n +=1


#C.Write a program to display each character from a string and if a character is number then stop the loop.
# x = "abcdefg"
# while "e"  in x:
#     print("The character e has been found at position", x.index("e"))
#     break
    


#D.Write a program to calculate the sum of series up to n term. For example, 
# if n=5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
# number_of_terms = 5
# sum1=0
# for i in range (1,number_of_terms+1):
#     num=eval('2'*i)
#     sum1+=num
# print(sum1)


#E.Create a program that prompts the user to enter a number, 
# then use a while loop to count from 1 up to the user's number.
# i = 1
# user_number = int(input("Please enter your number: "))
# while i < user_number:    
#     print(i)
#     i +=1


#F. Write a Python program that uses a while loop to print numbers from 1 to 10.
# i = 1
# while i <=10:
#     print(i)
#     i +=1


#G.Write a program that checks if a user-entered string is a palindrome (reads the same forwards 
# and backwards) using a while loop. Ignore spaces and letter case. a string from user & storing into variable.
# li = list(str) 
# ln = len(li) 
# i = ln - 1 

# while i >= 0: 
#     revStr = revStr + li[i]
#     i = i - 1 
# str = str.lower()
# revStr = revStr.lower() 

# if str == revStr: 
#     print(str, ", is PALINDROME!") 
# else:
#     print(str, ", isn't PALINDROME!") 


#H.Write a program that asks the user for an integer. If the number is even, divide it by 2, 
# if it's odd, multiply it by 3 and add 1. Repeat this process with the result until the result 
# becomes 1, and count how many steps it took.
# number = int(input("Enter your integer: "))
# while number <=100:
#     if number %2 == 0:
#         print("Even number is", number)
#         number +=1
        
#     else:
#         x = number *3
#         number+=1
#         print("odd number", x)


#I. Create a program that calculates the sum of all even numbers from 1 to a user-specified 
# number using a while loop.
# total = 0
# i = 2
# while i < 100:
#     total +=i
#     i +=2
#     print(i)


#J.Create a program that takes a list of numbers as input and reverses the list using a while loop. 
# Do this without using any built-in list reversal methods.
# number = int(input("Enter the integer number: "))
# revs_number = 0

# while (number >0):
#     remainder = number %10
#     revs_number = (revs_number *10)  + remainder
#     number = number //10
    
#     print("The reverse number is: ", revs_number)


#- Extra Hard -
# Task A:Count the total number of digits in a number . If user enters 547, the program should add each digit, so the output is 16 (as 5+4+7=16).
# num = int(input("Please enter your second: "))
# num2 = int(input("Please enter your first: "))
# num3 = int(input("Please enter third number: "))
# sum = (num+num2+num3)
# print("Sum number is:", sum)


#Task B:Write a program to display all prime numbers within a range.
# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper,"are:" )

# for num in range(lower, upper +1):
#     if num >1:
#         for i in range(2, num):
#             if(num % i) == 0:
#                 break
#             else:
#                 print(num)



# Task C:Create a program that takes a string as input and uses a while loop to reverse 
# and print the characters of the string.
# name= str((input("Enter the name: ")))
# i = len(name) - 1

# while i >= 0:
#     print(name[i], end = '')
#     i = i - 1



#Task D:Write a program that checks if a user-entered string is a palindrome (reads the 
# same forwards and backwards) using a while loop. Ignore spaces and letter case.
# str = input("Enter a string: ") 
# li = list(str)
# ln = len(li)
# revStr = ""
# i = ln -1

# while i >=0:
#     revStr = revStr + li[i]
#     i = i -1
#     str = str.lower()
#     revStr = revStr.lower()
    
#     if str == revStr:
#         print(str, ", is PALINDROME!")
#     else:
#         print(str, ", isn't PALINDROME!")


# Task E. Develop a program that takes an integer as input and prints a number pyramid using a 
# while loop. For example, if the user enters 5, the program should print:
#     1
#    121
#   12321
#  1234321
# 123454321

# row = int(input('Enter how many lines? '))
# for i in range(1,row+1):
#     for j in range(1, row+1-i):
#         print(' ', end='')
#     for j in range(1,i+1):
#         print(j, end='')
#     for j in range(i-1,0,-1):
#         print(j, end='')
#     print()


#ChatGPT's Homework-
# Task 1: Countdown Timer
# Write a program that uses a while loop to create a countdown timer. 
# Ask the user to enter a number of seconds, and then display a countdown 
# from that number down to 0.

# import threading
# import time

# def timer_function(seconds):
#     '''Countdown from number of seconds given'''
#     for t in range(seconds, -1, -1):
#         time.sleep(1)
#         print(t)


# if __name__ == "__main__":
#     print("Input minutes and seconds")
#     min = int(input("Minutes: "))
#     sec = int(input("Seconds: "))

#     x = threading.Thread(target=timer_function, args=(min * 60 + sec,))
#     x.start()
#     x.join()
#     print('All done')


# Task2: Number Guessing Game
# Create a number guessing game where the computer generates a random number, and the user has to guess it.Use a while loop to allow the user to keep guessing until they correctly guess the number.
# import random
# print("Hi welcome to the game, This is a number guessing game . \nYou got 7 chances to guess the number.Let's start the game")
# number_to_guess = random.randrange(100)
# chances = 7
# guess_counter = 0

# while guess_counter < chances:
#     guess_counter +=1
#     my_guess = int(input("Please Enter your Guess: "))
    
#     if my_guess == number_to_guess:
#         print(f"The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt")
#         break
    
#     elif guess_counter >= chances and my_guess != number_to_guess:
#         print(f"Oops sorry, The number is {number_to_guess} better luck next time")
        
#     elif my_guess > number_to_guess:
#         print("Your guess is higher")
        
#     elif my_guess < number_to_guess:
#         print("Your guess is lesser")



# Task 3: Factorial Calculator:Write a program that calculates the factorial of a given number using a while 
# loop. Ask the user for an integer input and compute its factorial.
# factorial = 1
# n = 1
# while True:
#     num = int(input("Enter number: "))
#     if num<=0:
#         print("Thank you! ")
#         break
#     while n <num:
#         n+=1
#         factorial *= n
#         print(factorial)



#Task 4:  Password Validation
# Implement a program that asks the user to enter a password. Use a while loop 
# to keep asking for the password until it matches a predefined correct password.      
# import re
# password = "R@m@_f0rtu9e$"
# flag = 0
# while True:
#     if (len(password)<=8):
#         flag = -1
#         break
#     elif not re.search("[a-z]", password):
#         flag = -1
#         break
#     elif not re.search("[A-Z]", password):
#         flag = -1
#         break
#     elif not re.search("[0-9]", password):
#         flag = -1
#         break
#     elif not re.search("[_@$]", password):
#         flag = -1
#         break
#     elif re.search("\s", password):
#         flag = -1
#         break
#     else:
#         flag = 0
#         print("Valid Password")
#         break
       
#     if flag == -1:
#         print("Not a Valid Password")


#Task 6:Sum of Even Numbers
# Calculate and display the sum of all even numbers from 1 to a user-defined 
# upper limit using a while loop.
# num = int(input("Enter number: "))
# while num<=20:
#     print(num)
#     num = num+1


#Task 7:  Multiplication Table: Generate and display the multiplication table for a given number using a while 
# loop. Ask the user for the number and the range (e.g., 1 to 10).
# multipler = 5
# counter = 1
# while counter <=10:
#     result = counter * multipler
#     print(f"{counter} * {multipler} = {result}")
#     counter +=1


#Task 8: Pattern printing
#Write a program that uses a while loop to print a pattern of asterisks, 
# where the number of asterisks on each line is equal to the line number. 
# For example:
# *
# **
# ***
# ****
# *****

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print()


#Task 9:Task with a for loop
# Create a program that uses both while and for loops.Ask the user for a number and print its multiplication table using a for loop inside the while loop.Continue asking for numbers until the user enters '0' to exit.
# n = int(input("Enter any Number: "))
# i = 1
# while i < 11:
#     for i in range(1,11):
#         value = n *i
#         print(n, " *", i, "=",value)
#         i = i +1


#Quiz-
# 1.What is the primary purpose of a while loop in Python?
# c)To repeatedly execute a block of code as long as a specified condition remains true.

#2.What are some best practices for using while loops in Python?
# b)Use vague variable names to encourage creativity


#3.What should you consider when using a while loop in Python?
# d)Using while loops for all types of iterations


#4.What are the key differences between while and for loops in Python?
# a) While loops are primarily used for iteration, while for loops are used for conditional execution.


#5.What is the potential risk of using an infinite while loop in your code?
#b)It can lead to unexpected program termination.


#6.How do you ensure that a while loop will terminate and not result in an infinite loop?
#a) By not using while loops at all.


#7.Which of the following statements is true about the loop control variable in a while loop?
#d)It is optional and not required for a while loop.


#8.In Python , what happens when the condition of a while loop is initially False?
#a)The loop is skipped entirely,and the code continues after the loop.


#9.What is an off-by-one error in the context of while loops?
#a)An error that occurs when the loop control variable is not properly initialized.

#10.What is the output of the following code?
# count = 1
# while count <=5:
#     print(count)
#     count +=1

#a)12345


#11.What is the output of the following code?
# while True:
#     print("Infinite Loop")

#a)Infinite Loop


#12.What is the output of the following code?
# count = 1
# while count <=10:
#     if count ==5:
#         break
#     print(count)
#     count +=1

#b)1 2 3 4


#13.What is the output of the following code?
# count = 1
# while count <=5:
#     if count %2 ==0:
#         count +=1
#         continue
#     print(count)
#     count +=1

#b)1 3 5


#14.What is the output of the following code?
# outer_count = 1
# while outer_count <=3:
#     inner_count = 1
    
#     while inner_count <=2:
#         print(outer_count, inner_count)
#         inner_count +=1
#         outer_count +=1

#e) None of the above


#15.What is the output of the following code?
# num = 5
# fact = 1
# while num>0:
#     fact *=num
#     num -=1
#     print(fact)
# a)120



#16.What is the output of the following code?
# total = 0
# while True:
#     num = int(input("Enter a number (0 to exit):"))
#     if num ==0:
#         break
#     total +=num
#     print("Sum:", total)

#a) The program adds numbers until the user enters 0 and then displays the sum.


# 17.What is the value of x:
# x = 0
# while(x <100):
#     x +=2
#     print(x)
#d)100


#18.What is the output of the following if statement :
# a, b = 12,5
# if a +b:
#     print('True')
# else:
#     print('False')

#b)True


#19.What is the value of the var after the for loop completes its execution:
# var = 10
# for i in range(10):
#     for j in range(2,10,1):
#         if var %2 ==0:
#             continue
        
#         var+=1
#     else:
#         var+=1
#         print(var)


#b)21


#20.What is the output of the following nested loop:
# for num in range(10,14):
#     for i in range(2, num):
#         if num %i ==1:
#             print(num)
#             break

#a)10
#11
#12
#13


#21.What is the output of the following nested loop:
# numbers = [10,20]
# items = ["Chair", "Table"]
# for x in numbers:
#     for y in items:
#        print(x, y)


#a)10 Chair
# 10 Table
# 20 Chair
# 20 Table


#For Loops-
#A.Write a program to use the loop to find the factorial of a given number.
# n = 23
# fact = 1
# for i in range(1,n+1):
#     fact = fact *i
#     print("The factorial of 23 is:", end="")
#     print(fact)


#B.Write a program that uses a for loop to print numbers from 1 to 10.Homever, if the number is divisible by 3, skip the loop, and if the number is 7, stop the loop.
# for num in range(1,11):
#     if num /3 :
#         print(num)
#         continue
#     elif num /7:
#         break
#     print(num)


#C.In Python, what is the purpose of the range() function when used with a for loop?
#The function range() returns a sequence of numbers starting from 0 and increasing (by default) to 1, stopping before the specified number.


#D.How can you prematurely exit a for loop in Python?
#If you want to leave a loop early in Python you can use break, just like in Java.If you want to start the next iteration of the loop early you use continue, again just as you would in Java.


#E.What is an iterator in Python, and how is it related to for loops?
#An iterator is essentially a value producer that yields successive values from its associated iterable object.


#F.How can you iterate through the elements of a list in reverse order using a for loop?
#Using reversed() Method
#The simplest way to perform this is to use the reversed function for the for loop and iteration will start occuring from the rear side than the conventional counting.


# G.Create a for loop that prints all even numbers from 20 to 40.Solve this task in two different ways (modifying range() and using if statements).
# for num in range(20,41):
#     if num%2 ==0:
#         print("Even Numbers", num)
#     else:
#         print("Odd numbers", num)


#H.Write a for loop to calculate the sum of all integers from 1 to 100. At the end of the loop the program should print 'The end of a task'.
# total_sum = 0
# for i in range(1,101):
#     total_sum += i 
#     print("The sum of integers from 1 to 100 is:", total_sum)



#I.Generate a multiplication table for a given number using a for loop, e.g., for the number 5, print 5x1, 5x2, ..., 5x10
# num = int(input("Enter number: "))
# for i in range(1,11):
#     print(num , 'x', i, '=', num *i)


# J.Write a for loop to iterate through a string and print each character on a separate line with corresponding index.
# string = input("Enter string: ")
# for char in string:
#     print(char)


# K.Suppose you have the following list:
# employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]
# #Iterate over this list and print all names except the ones which start with the letter 'J'.
# for name in employees:
#     if not name.startswith('J'):
#         print(name)

#L.Suppose you have the following list:
# stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]
# Iterate over this list and print all fruits and vegetables except the ones which start with the letter 'C' and whichs length is less than or equal 6.
# for item in stock:
#     if not(item.startswith('C')or len(item)<=6):
#         print(item)    


#M.Write a for loop to reverse a given string. For example, "hello" should become 'olleh'.
# You shouldn't use any reversing methods such as [::-1]. Instead you should make manipulations
# with string literals
# N = input("Enter your word: ")
# print("The reversed numbers are:", end= "")
# for text in reversed (N):
#    print(text, end= " ")


#N.Write a for loop to check and print all prime numbers within a given range(on dynamic user input).
# lower = 100
# upper = 10000
# print("Prime numbers between", lower, "and", upper, "are: ")
# for num in range(lower, upper +1):
#    if num > 1:
#       for i in range(2, num):
#          if(num %i) ==0:
#             break
#          else:
#             print(num)
#             break



#O.Implement a for loop to search for a spesific word in a text and replace it with another word.
# MyStr2 = "I am poor"
# d = {'poor': 'Good'}

# print(' '.join(d.get(t, t) for t in MyStr2.split()))


# P.Write a program that draws the pyramid as:
# Reverse Pyramid:
#   ***********     
   # *********
   #  *******
   #   *****
   #    ***
   #     *
# rows = 5
# k = 2 * rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")


#Q.Write the shortest program that prints the position and each character of a string.
# string = 'new string'
# pattern = 'rg'

# index = []
# for x in range(len(pattern)):
#    if pattern[x] in string:
#       index.append(string.index(pattern[x]))
      
#       index.sort()
      
#       l= len(index)
#       low = int(index[0])
#       high = int(index[l-1])
#       h = high + 1
#       for i in range(low , h):
#          print(string[i], end=" ")



#R.You have the following dictionary:
# data = {
#    "key1":80,
#    "key2": 75,
#    "key3": 65,
#    "key4":85
# }
# Iterate over it and check if any value is less than 80, add the missing points.
# for key , value in data.items():
#    if value < 80:
#       data[key] = 80
#       print(data)


#S.Copy this code to your file:
# from random import randint
# numbers = [randint(15,40) for _ in range(5)]
# print(numbers)
# max_value = numbers[0]
# for num in numbers:
#    if num > max_value:
#       max_value = num
#       print(max_value)
# This gives you a list of 5 random numbers between 15 and 40.Using for loops find the max value of that list, and print the list to see values.


#T.Use 'numbers' list from Task S.Iterate over it again , and if there is a number between 20 and 25 exit the loop,otherwise print the value.
# if 20<= num <=25:
#    print(num)
# else:
#    print(num)

#U.Write a Python program to construct the following pattern:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")


#V.Write a Python program to count the number of even and odd numbers in a collection of numbers.
# numbers = (1,2,3,4,5,6,7,8,9)
# count_odd = 0
# count_even = 0
# for i in numbers :
#    if i %2 ==0:
#       count_even +=1
#    else:
#       count_odd +=1
#       print("Number of even numbers:",count_even)
#       print("Number of odd numbers:", count_odd)


#W.Write a Python program that prints each item and its corresponding type from the following list.
# [5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]
# datalist = [5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]
# for item in datalist:
#    print("Type of", item, "is", type(item))


# X. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for x in range(6):
#    if(x ==3 or x ==6):
#       continue
#    print(x, end='')
#    print("\n")


#Y.Write a Python program that accepts a string and calculates the number of digits and letters.
# s = input("Input a string: ")
# d = l = 0
# for c in s:
#    if c.isdigit():
#       d = d+1
#    elif c.isalpha():
#       l = l+1
#    else:
#       pass
#    print("Letters", l)
#    print("Digits", d)


#Z.Write a Python program to guess a number between 1 and 9. The program should use 'random' module,
# give only 3 chances to guess the number. Print 'Congratulations' if you guess and 'Game Over'
# if you fail.
# import random
# number = random.randint(1,9)
# chance = 3
# if number == number:
#  num = int(input("Please enter your num: "))
# print("Congratulations!!")
# print("Exit game")



#Chat GPT's Homework-
#Problem1: Generate a Series
#Write a Python program that uses a for loop to generate and print the following series of numbers: 1,4,9,16,25,... up to a given positive integer n.The series consists of perfect squares.
# i = (1,4,9,16,25)
# for i in range(1,11):
#    sq = i *i
#    print(sq, end=" ")


#Problem 2: Calculate Factorial with a For Loop
# Write a Python program that calculates the factorial of a given positive integer n using a for loop.Display result.
# n = int(input("Enter n:"))
# fact = 1
# for i in range(2, n+1):
#    fact *=i
#    print("Factorial of {} is: {}".format(n, fact))


#Problem 3: Password Generator
# Write a Python program that generates a random password consisting of both uppercase 
# and lowercase letters, digits, and special characters. The password should be of a 
# specified length n. Use a for loop to create the password.
# import string
# import random

# length = int(input("Enter password lenght: "))
# print('''Choose character set for password from these : 
#          1. Digits
#          2. Letters
#          3. Special characters
#          4. Exit''')
# characterList = ""
# while(True):
#    choice = int(input("Pick a number"))
#    if(choice ==1):
#       characterList +=string.ascii_letters
      
#    elif(choice ==2):
#       characterList +=string.digits
      
#    elif (choice ==3):
#       characterList +=string.punctuation
      
#    elif (choice ==4):
#       break
#    else:
#       print("Please pick a valid option!")
      
# password = []
# for i in range(length):
#    randomchar = random.choice(characterList)
#    password.append(randomchar)
#    print("The random password is:" + "".join(password))



#Problem 4:Average of Numbers
# Write a Python program that calculates the average of a list of numbers using a 
# for loop. Prompt the user to enter a list of numbers (comma-separated), and then 
# compute and display the average.
# list = [30,55,3,10,2]
# sum = 0
# for num in list:
#    sum +=num
#    average = sum/len(list)
#    print("The average of the list is:", average)



#Problem 5:Pattern Printing:
# Write a Python program that prints the following pattern using nested for loops:
# 1
# 12
# 123
# 1234
# 12345
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')



#Problem 6: Count Vowels and Consonants
# Write a Python program that counts the number of vowels and consonants in a given 
# string. Use a for loop to iterate through the characters of the string and 
# categorize them as vowels or consonants. Display the counts separately.
# input_string = "Python Programming"
# vowels = "aeiouAEIOU"
# consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
# vowel_count = 0
# consonant_count = 0

# for char in input_string:
#    if char in vowels:
#       vowel_count +=1
#    elif char in consonants:
#       consonant_count +=1
      
#       print(f"Vowels: {vowel_count}")
#       print(f"Consonants: {consonant_count}")



#Problem 7: Reverse a List
# Write a Python program that takes a list as input and uses a for loop to reverse 
# the order of elements in the list. Display the reversed list.
# my_list = [1,2,3,4,5]
# new_list = []
# for i in range(len(my_list)):
#    new_list.insert(i, my_list[-1])
#    my_list.pop(-1)
#    print(my_list)


#Problem 8:Finding Factors
# Write a Python program that prompts the user to enter a positive integer and 
# then finds and prints all the factors of that integer using a for loop.
# def print_factors(x):
#    print("The factors of",x,"are:")
#    for i in range(1, x + 1):
#        if x % i == 0:
#            print(i)

# num = 320

# print_factors(num)


#Quiz-
#1.How do you terminate a 'for' loop prematurely in Python?
# a)Using 'break'


#2.What is the syntax for a 'for'loop in Python?
#b)for i in range(5)


#3.Which statement is used to skip the current iteration and continue to the next in a 'for' loop?
#c)continue

#4.What is the maximum number of times a 'for' loop can iterate?
#d) There is no maximum limit


#5.Which data types can be iterated over using a 'for' loop in Python?
#b)Lists and dictionaries


#6.In a 'for' loop, how can you access both the index and value of each element in a list?
# a)Use a while loop instead

