def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y==0:
        return "MathError!"
    else:
        return x/y
    
def calculations(operation,num1,num2):
    if operation == "1":
        return f"{num1}+{num2}={add(num1,num2)}"
    elif operation == "2":
        return f"{num1}-{num2}={subtract(num1,num2)}"
    elif operation == "3":
        return f"{num1}*{num2}={multiply(num1,num2)}"
    elif operation == "4":
        result = division(num1,num2)
        if result == "MathError":
            return "MathError occurred"
        else:
            return f"{num1}/{num2}={result}"
    elif operation == "5":
        return "Exiting the calculator"   
    else:
        return "Invalid input. Please enter a valid input."
    
def main():
    while True:
        print("Select Operation to perform:")
        print("1. add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")
    
        operation = input("Choose an operation 1/2/3/4/5:")
        
        if operation == "5":
            print("Exiting the calculator!!")
            break
        
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        
        print(calculations(operation,num1,num2))
        
if __name__ == "__main__":
    main()      
        
            
    
    
