for _ in range(3):
    try:
        # Get user input and convert it to an integer
        a = int(input("Enter a number: "))
        
        # Check if the number is even or odd
        if a % 2 == 0:
            print(f"{a} is even.")
        else:
            print(f"{a} is odd.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input! Please enter a valid integer.")
