# Input the number of elements in the array
N = int(input())

# Input the array elements
arr = list(map(int, input().split()))

# Create a set to store unique values
unique_values = set()

# Iterate through the array and add each element to the set
for num in arr:
    unique_values.add(num)

# Convert the set back to a list to maintain the order
result = list(unique_values)

# Print the unique values
print(*result)
