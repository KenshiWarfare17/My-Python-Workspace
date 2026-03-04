def display_menu():
    print("1. Bego")
    print("2. TAI")
    print("3. cibai")
    print("4. Pergi lu")

def option1():
    print("You selected Option 1.")

def option2():
    print("You selected Option 2.")

def option3():
    print("You selected Option 3.")

# Main program
while True:
    display_menu()
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")