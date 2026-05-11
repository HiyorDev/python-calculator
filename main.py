# - - -
# - -
# -


#Imports
import operations
import time

# List used to store the history of operations
results_list = []


# Function that displays the calculator menu
def menu():

    print("\n== Calculator ==")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Attempt to read the user's menu option
    try:
        option = int(input("Enter an option: "))
        return option

    # Handle invalid input errors
    except ValueError:
        print("Invalid option")
        return 0


# Main function that runs the calculator
def main():

    # Infinite loop until the user exits
    while True:

        # Small delay for better user experience
        time.sleep(1)

        # Display menu and get user option
        option = menu()

        # Perform addition
        if option == 1:

            result = operations.addition()

            # Save result if operation was successful
            if result is not None:
                results_list.append(result)

        # Perform subtraction
        elif option == 2:

            result = operations.subtraction()

            if result is not None:
                results_list.append(result)

        # Perform multiplication
        elif option == 3:

            result = operations.multiplication()

            if result is not None:
                results_list.append(result)

        # Perform division
        elif option == 4:

            result = operations.division()

            if result is not None:
                results_list.append(result)

        # Exit the calculator
        elif option == 5:

            # Display operation history
            print(f"\nToday's history: {results_list}")

            print("Closing calculator...")

            time.sleep(1)
            break

        # Handle invalid menu options
        else:
            print("Invalid option, try again")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()