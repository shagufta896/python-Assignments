 #WAP That Search for Prime Numbers from 15 through 25*

for num in range(15, 26):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
