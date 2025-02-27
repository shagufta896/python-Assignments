
### Read Marks of Six Subjects and Display Results


marks = []
for i in range(6):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))

print("Marks in each subject:", marks)
print("Total marks:", sum(marks))
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
