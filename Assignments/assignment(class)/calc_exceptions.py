try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = (a + b) / b
    print("Result:", result)

except TypeError:
    print("Wrong data type used in calculation.")

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
