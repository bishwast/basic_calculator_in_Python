"""Add, subtract and divide"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd num: "))
operator = input("Enter operator: ")

if operator == '+':
    print(f"The addition is {num1} + {num2} as: ", num1+num2)
elif operator == "-":
    print(f"Your substraction is {num1} - {num2} as: ", num1-num2)
elif operator == "/":
    print(f"You divided {num1} by {num2} as: ", abs(num1/num2))
elif operator == "*":
    print(f"The product of {num1} and {num2} is: ", num1*num2)
elif operator == "%":
    print(f"Modulus of {num1} and {num2} is: ", num1%num2)
else:
    print("Operator does not exist in this calculator.")

    
