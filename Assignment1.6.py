from statistics import mean, median, mode

# Function to calculate mean, median, and mode
def calculate_statistics(marks):
    try:
        # Calculate mean
        mean_value = mean(marks)
        
        # Calculate median
        median_value = median(marks)
        
        # Calculate mode
        mode_value = mode(marks)
        
        return mean_value, median_value, mode_value
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

# Input: Obtain marks from the user
marks = []
n = int(input("Enter the number of students: "))

for i in range(n):
    mark = float(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

# Calculate statistics
mean_value, median_value, mode_value = calculate_statistics(marks)

# Display results
if mean_value is not None:
    print(f"\nMean of marks: {mean_value:.2f}")
    print(f"Median of marks: {median_value:.2f}")
    print(f"Mode of marks: {mode_value:.2f}")
else:
    print("Unable to calculate statistics.")