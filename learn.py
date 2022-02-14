#PYTHON LOOPS
#For loop
fruits = ['apple', 'peach', 'pair']
for fruit in fruits:
    print(fruit)

#coding exercise: average heights exercise:
#calculating the average of heights input
student_heights = input("Enter the student heights separated by a space: ").split( )
summation = 0
for n in range(0, len(student_heights)):
    summation += int(student_heights[n])
print(f"The average students heights is {round(summation/len(student_heights))}")
# otherwise, there is the sum(my_list) function that prints the total sum

# coding exercise 2: print heighest score from a list of scores
# max(my_list) function prints the maximum value (no using it in this challenge) same to min(my_list) function
student_scores = input("Input student scores seperated by a space: ").split( )
max_score = 0
for score in student_scores:
    if int(score) > max_score:
        max_score = int(score)

print(f"The maximum score in the list is: {max_score}.")

# for loop with the range() function
for number in range(1, 10):#executes for 1 to 9 without 10
    print(number) #prints 1 to 9

# specifying a step value
for number in range(1, 10, 3):
    print(number)#1 4 7

# coding exercise, adding evens
# adding all even numbers between 1 and 100
summation = 0
for number in range(2, 101, 2):
    summation += number
print(f"All even numbers between 1 and 100 add to {summation}")

# CODING CHALLENGE: FIZZBUZZ
# your number should print 1 to 100
# if the number is divisible by 3, instead of printing it, print fizz, by 5, print buzz by fizzbuzz if it is divisible by both 3 and 5
for number in range(1, 101):
    if number%3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

