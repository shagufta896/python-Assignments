
###  Create a List of Numbers from 1 to 10 and Delete Even Numbers*


numbers = list(range(1, 11))
numbers = [num for num in numbers if num % 2 != 0]
print("List after deleting even numbers:", numbers)

