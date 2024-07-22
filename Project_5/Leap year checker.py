def main():
    
    while True:
        # Place the input method inside the loop for it prompt the user to enter a new year when the previous year is not a leap year.
        year = int(input("What is the year?"))
        
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"The year {year} is a leap year.")
            break
        else:
            print(f"The year {year} is not a leap year. Please enter another year.")
            
            
main()