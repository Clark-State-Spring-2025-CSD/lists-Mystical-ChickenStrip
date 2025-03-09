#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class

import statistics

# Prompt the user to enter 5 numbers and store them in a list
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}/5: "))
    numbers.append(num)

# Display the list as entered
print("\nNumbers as entered:", numbers)

# Display the list sorted small to large
sorted_numbers = sorted(numbers)
print("Numbers sorted (small to large):", sorted_numbers)

# Display the list sorted large to small
print("Numbers sorted (large to small):", sorted_numbers[::-1])

# Calculate and display the mean and median
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
