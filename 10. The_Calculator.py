
def calculate(a,b,operator):
    if operator == "+":
        return (a+b)
    
    elif operator == "-":
        return (a-b)
    
    elif operator == "*":
        return (a*b)
    
    elif operator == "/":
        return (a/b)

first_number = float(input("What's the first number?: "))

while True:        

        print("+\n-\n*\n/")

        operator = input("pick an operation: ")

        second_number = float(input("What's the next number?: "))

        result = calculate(first_number, second_number, operator)
        print(result)

        continue_calculation = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation: ").lower()
        first_number = result

        if continue_calculation != 'y': 
            break
        
        print(f"Result = {result}")
      



