def temp_converter():
    temp = float(input("What is the temperature:"))
    units = input("Enter the units C for Celcius , F for Fahrenheits:")
    
    if units.upper() == "C":
        converted = (temp * 9/5) + 32
        print(f" {temp} Celcius is {converted} Fahrenheits")
    elif units.upper() == "F":
        converted = (temp-32)* 5/9
        print(f"{temp} Fahrenheits is {converted} Celcius")
    else:
        print("Invalid input")
        
temp_converter()
        