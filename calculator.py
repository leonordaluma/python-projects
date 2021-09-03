def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
function = operations[operation_symbol]
answer = function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("Enter the next number: "))
function = operations[operation_symbol]
answer2 = function(answer, num3)
print(f"{answer} {operation_symbol} {num3} = {answer2}")