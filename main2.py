age = 18

if age >= 18:
    print ("You can vote.")
else:
    print("You cannot vote yet")


# if condition1:
    #if condition2:

    #else:

    #else

temperature = 28

if temperature > 30:
    print("Its a hot day, stay hydrated.")
elif 20 <= temperature <= 30:
    print("The weather is pleasant.")
else:
    print("Its a cold day")

student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a partial scholarship.")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is eligible for a full scholarship.")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")
else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")


names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print(name)


sentence = "Hello, World"

for character in sentence:
    if character.isalpha():
        print(character)

for number in range(1, 6):
    print(number)


numbers = [12, 45 ,6 ,72, 21,8, 94, 57]

#Initialize a variable "maximum" with the first value from the list "numbers".
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum value in the list is:", maximum)


count = 1

while count <= 5:
    print("Iteration", count)
    count +=1

numbers = [1,2,3,4,5,6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target Found!")
        break



scores = [68,42,57,78,35,62,50,92]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue
    total += score
    count += 1


average = total / count if count > 0 else 0

print("Average score for scores above 50:", average)

while True:
    user_input = input("Enter a positive number: ")

    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break
    
    print("Invalid Input. Please Try again")
print("You entered a valid positive number:", number)


sum_even = 0

for num in range(1, 11):
    if num % 2 == 0:
        sum_even += num

print("Sum of even numbers from 1 to 10:", sum_even)


def greet():
    print("Hello World")

greet()

def greet_person(name):
    print("Hello", name)


greet_person("Alice")

#result = add(3,7)

#print("3+7=", result)


def greet(name):
    message = f"Hello, {name}"

    print(message)
greet("Alice")

greeting = "Hello"

def greet(name):
    message = f"{greeting}, {name}!"
    print(message)

greet("Bob")

print(greeting)

greeting = "Hello"

def greet(name):
    global message
    message = f"{greeting}, {name}!"

    print(message)


greet("Doris")

print(message)

message = f"{greeting}, student!"

print(message)


greeting = "Hello"
name = "Plator"

def greet():
    global greeting
    greeting = "Goodbye"
    name = "Alice"
    message = f"{greeting}, {name}!"
    print(message)

greet()

print(greeting)

print(name)