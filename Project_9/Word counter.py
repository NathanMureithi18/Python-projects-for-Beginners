def counter():
    while True:
        print("Choose how you want input your file: ")
        print("1. Enter Text Manually")
        print("2. Load Text from File")
        print("3. Exit")
        
        input_method = input("Choose which method to use to input your file: ")
        
        if input_method == "1":
            text = input("Enter your text here: ")
            words = text.split()
            print(f"The text has {len(words)} words.")
        elif input_method == "2":
            file_name = input("Enter the name of the file: ")
            with open(file_name,'r') as file:
                text = file.read()
            words = text.split()
            print(f"The text has {len(words)} words.")
        elif input_method == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose from the menu.")

# Call the function once, without recursion
counter()