print("*************Your Phonebook!! *************")
# Open the file in write mode. Delete the file it already exists
with open("phonebook.txt", "w") as file:   
        file.write("Name: Number\n")

## Niraj notes: This is inefficient as it writes every entry as soon as the user enters it. A better way could be to store the entries in a list and write them all at once at the end.
while True:
    name = input("Enter contact name: ")
    phone_number = int(input("Enter phone number: ").strip())  #Niraj notes: strip() removes leading and trailing spaces
    with open("phonebook.txt", "a") as file:    #Niraj notes: using 'a' will append the file
        file.write(f"{name}:{phone_number}\n")
    done_adding = input("Do you want to add another contact? (yes/no): ")
    if done_adding.lower() == "no":
        break
    else:
        print("Added contact successfully")

