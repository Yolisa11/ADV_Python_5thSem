try:
    num = float(input("Enter a number: "))
    result = num / 2
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")
