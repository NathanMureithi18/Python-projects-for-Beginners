# Add Contact: Function to add a new contact to the list.
contacts = []
contacts.append({'Name': 'John', 'Phone number': '1234567890', 'Email': 'john@example.com'})
contacts.append({'Name': 'Jane', 'Phone number': '0987654321', 'Email': 'jane@example.com'})

def contact_list():
    print("Choose the operation to perform: ")
    print("1. Add contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    operation = input("Choose the operation to perform: ")
    if operation =="1":
        n = int(input("Enter the number of contacts to add: "))
        def add_contact():
            
            for i in range(1,n+1):
                Name = input(" Enter the Name of contact: ")
                phone_number = int(input("Enter the phone number: "))
                email = input("Enter email address: ")
                
                contact_details = {'Name': Name,'Phone number': phone_number,'Email': email}
                contacts.append(contact_details)
                
                # print(contacts)

        add_contact()

    elif operation == "2":
        # View Contacts: Function to display all contacts.
        def view_contact():
            for contact in contacts:
                print(f"Name : {contact['Name']}, Phone number : {contact['Phone number']}, Email : {contact['Email']}")
                
        view_contact()  

    elif operation == "3":
        # Update Contact: Function to update an existing contact.
        def update_contact():
            cont_Name = input("Enter the Name to update")

            for contact in contacts:
                if contact['Name']== cont_Name :
                    print("1.Phone number")
                    print("2.Email")
                    details_update = input("Choose the details you want to update(1 or 2):  ")
                    
                    if  details_update == "1":
                        new_phone_number = input("Enter the new phone number: ")
                        contact["Phone number"] = new_phone_number
                        print(f"Phone number for {cont_Name} updated successfully.")
                        
                    elif details_update == "2":
                        new_email = input("Enter the new email: ")
                        contact["Email"] = new_email
                        print(f"Email for {cont_Name} updated successfully.")
                    else:
                        print("Invalid choice. Please choose either 1 or 2: ")
                    break
                        
            else:
                print("No contact was found with that name!!")
                
        update_contact()
    
    elif operation == "4":
        # Delete Contact: Function to delete a contact by Name
        def delete_contact():
            cont_name = input("Enter name of the contact to delete")
            
            for contact in contacts:
                if contact['Name']== cont_name:
                    contacts.remove(contact)
                    print(f"Details of {cont_name} successfully deleted.")
                    break
            else:
                print("No contact was deleted!!. Please enter the name correctly.")
        delete_contact() 
    
    else:
        print("Invalid operation. Please choose a number between 1 and 4.")

        
        
contact_list()
    
        


    
    