## Add corresponding elements of two lists:

L = [1, 2, 3, 4]
M = [5, 6, 7, 8]
N = [L[i] + M[i] for i in range(len(L))]
print("Sum of corresponding elements:", N)
