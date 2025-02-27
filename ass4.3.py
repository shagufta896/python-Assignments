#check number and then check is it positive negative or zero.

# Input: Ask the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")


