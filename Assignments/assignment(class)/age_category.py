try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age < 18:
        print("You are a child.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior.")

except ValueError:
    print("Invalid input. Please enter a valid integer age.")
