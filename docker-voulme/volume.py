try:
    # Prompt the user for a name
    name = input("Enter your name: ")
    
    # Open the file in append mode to add the name
    with open("user_info.txt", "a") as file:
        file.write(name + "\n")
    
    # Ask the user if they want to read all names
    choice = input("Do you want to read all the names from the file? (y/n): ").strip().lower()
    
    if choice == 'y':
        # Open the file in read mode and print its content
        with open("user_info.txt", "r") as file:
            print("\nNames in the file:")
            for line in file:
                print(line.strip())
    else:
        print("Alright, names not displayed.")
except Exception as e:
    print("An error occurred:", e)