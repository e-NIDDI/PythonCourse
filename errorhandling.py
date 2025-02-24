age = 25

age_as_str = str(age)

print (age_as_str, "of type", type(age_as_str))


print(bool(0))

print(bool(42))


print(bool(""))
print(bool("Hello"))

print(bool([]))
print(bool(None))

x = 32
y = 5.3

result = x + y
print(result, "of type", type(result))

age = 25
message = "I am" + str(age) + " years old"
print(message)

a = 5
b = "3"
result1 = a * int(b)
print(result1, "of type", type(result1))

#z = int("abc")
#Value Error Invalide Literal for int()

name = input("Enter Your Name:")
print(f"Hello, {name}")

age = input("Enter Your Age:")

print(type(age))

number1 = int(input("Enter a valid first number:"))

number2 = int(input("Enter the second number:"))

result = number1 + number2

print(f"The sum of {number1} and {number2} is {int(result)}")

try:
    result = 10/0
except ZeroDivisionError:
    print("Oops! Tried to devide with zero")

fruits = {
    "apple": 5,
    "banana":7,
    "orange": 3
}

try:
    print(fruits["cherry"])

except KeyError:
    print("The Key does not exist in the dictionary")


text = "This is not a number"

try:
    text_to_int = int(text)

except Exception as e:
    print("An error occurred while parsing the data: ", e)

try:
    result = 10/2
except ZeroDivisionError:
    print("Division by zero error occurred")
else:
    print("Division Successful. Result:",result)


try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot Divide By Zero.")
finally:
    print("Finally Blox Executed")



def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Invalid divison by zero.")
    except TypeError:
        print("Invalid type for divison.")
    except Exception as e:
        print(f"Unexpected error: {e}")

divide_numbers(3,4)