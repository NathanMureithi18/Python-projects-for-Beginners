def factorial(n):
    result = 1
    if n < 0:
        return None
    
    if n > 0:
        for i in range(1, n+1):
            result *=i
        return result
    if n == 0:
        return result
    
while True:
    number = int(input("Please enter a number: "))
    
    if number < 0:
        print("The number you entered is negative. Please enter a positive number: ")
        continue
    
    if number is not None:
        factorial_n = factorial(number)
        print(f"The factorial of the number {number} is {factorial_n}")
        break
    
    