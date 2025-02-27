### WAP Print First n Odd Numbers in Descending Order


n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    print(2 * i - 1, end=" ")

