from art import logo
print(logo)






# addition 
def add(n1 , n2):
    return n1 + n2

# subtraction 
def subtract(n1 , n2):
    n1 - n2

# multiplication 
def multiply(n1 , n2):
    n1 * n2

# division 
def divide(n1, n2):
    n1 / n2

operations = {
   "+":  add,
   "-": subtract,
   "*": multiply,
   "/": divide
}

num1 = int(input("What's the first number? \n"))
num2 = int(input("What's the second number? \n"))

for operators in operations:
    print(operations[operators])


print(operations)