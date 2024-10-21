#Exercise1 :
#write the python program to perform the following operations
#1.Add,subtract,multify,and divide two numbers(input by the user)
#2.Use the modulus operator to find the remainder of their division

'''a=int(input('enter the number please:'))
b=int(input('enter the number please:'))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)'''

#Exercise 2
'''Write a Python program that asks for two numbers and checks: 
1.If the first number is greater than the second. 
2.If the first number is equal to the second. 
3.If the first number is less than or equal to the second'''

'''a=int(input('enter the number:'))
b=int(input('enter the number:'))
if a>b:
    print('the first number is greater than the second number')
elif a==b:
    print('the first number is equal to second number')
else:
    if a<=b:
        print('first number is less than or equal to the second number')'''


#Exercise 3: Logical Operators 
#Write a Python program that:
#Takes three boolean values(True or False) as input
'''a=10
b=20
c=5
print(a>b)
print(a<b)
print(b<c)'''
#Use and ,or and not operators to return the result of combining them
'''a=10
b=20
c=30
print(a<b and a>b or a==b not c>a)'''


#Part 2: Strings 
#Exercise 4: String Manipulation 
#1.Take a string input from the user.
'''a=str(input('enter the your name please:'))
print(len(a))
print(a[::-1])
print(a.lower())
print(a.upper())
print(a[0::5])'''


#Exercise 5: String Formatting 
#Write a program that asks for the user's name and age,
#and displays the message in this format:

'''a=str(input('enter the your name please:'))
b=str(input('enter the your age please:'))
print(f"Hello {a}, you are {b} years old.")'''

#Exercise 6: Substring Search
#Write a Python program that: 
#1.Asks for a sentence input from the user. 
#2.Asks for a word to search in the sentence.
#3.Outputs whether the word exists in the sentence and,
#if it does, at which position (index).

'''a=str(input('enetr the sentence please:'))
print(a.find('alliance'))
print(a.index('alliance'))'''


#Lists
#Exercise 7: List Operations
#Write a Python program that: 
#1.Creates a list of 5 numbers (input from the user). 
#2.Displays the sum of all the numbers in the list. 
#3.Finds the largest and smallest number in the list.


'''numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


total_sum = sum(numbers)


largest_number = max(numbers)
smallest_number = min(numbers)


print("\nSum of all numbers:", total_sum)
print("Largest number:", largest_number)
print("Smallest number:", smallest_number)'''

#Exercise 8: List Manipulation

#1.Create a list of 5 of your favorite fruits. 
#Perform the following: 
#1)Add one more fruit to the list. o
#2)Remove the second fruit from the list. o 	P
#3)rint the updated list.

'''a=['apple','banana','orange','watermelon','mango']
a.append('strawberry')
print(a)
a=['apple','banana','orange','watermelon','mango']
a.remove(2)
print(a)'''

#Exercise 9: Sorting a List 
#Write a Python program that: 
#1.	Asks the user to input a list of 5 numbers. 
#2.	Sorts the list in ascending order and displays it. 
#3.	Sorts the list in descending order and displays it. 


numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)


ascending_order = sorted(numbers)
print("\nList in Ascending Order:", ascending_order)


descending_order = sorted(numbers, reverse=True)
print("List in Descending Order:", descending_order)



#Exercise 10: List Slicing 
#Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], perform the following: 
#1.	Print the first 5 elements. 
#2.	Print the last 5 elements. 
#3.	Print the elements from index 2 to index 7. 



'''a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=a[0:5]
print(b)
b=a[5:10]
print(b)
b=a[2:8]
print(b)'''

#Bonus Challenge 
#Write a Python program that: 
#1.	Takes input of 3 students' names and their respective scores in 3 subjects. 
#2.	Stores them in a nested list. 
#3.	Prints each student's name and their average score. 

'''students = []
for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    scores = []
    for j in range(3):
        score = float(input(f"Enter the score for subject {j+1}: "))
        scores.append(score)
    
    students.append([name, scores])
print("\nStudent Name and Average Score:")
for student in students:
    name = student[0]
    scores = student[1]
    average_score = sum(scores) / len(scores)
    print(f"{name}: {average_score:.2f}")'''








