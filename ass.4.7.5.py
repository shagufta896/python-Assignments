number = input("Enter a number: ")
digits = [int(d) for d in number]

#Frequency of digits
freq = {}
for d in digits:
    freq[d] = freq.get(d, 0) + 1
print("Frequency of digits:", freq)
