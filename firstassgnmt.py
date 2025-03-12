number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

sub = number1 - number2
print(f"{number1} - {number2} = {sub}")

add = number1 + number2
print(f"{number1} + {number2} = {add}")

mult = number1 * number2
print(f"{number1} * {number2} = {mult}")

if number2 != 0:
    div = number1 / number2
    print(f"{number1} / {number2} = {div}")
else:
    print("Division by zero is not allowed.")
