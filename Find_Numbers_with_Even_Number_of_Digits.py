# Input the length of the array
n = int(input())

# Input the array elements as a list of integers
nums = list(map(int, input().split()))

# Initialize a variable to count the numbers with an even number of digits
count = 0

# Iterate through the elements of the input array
for num in nums:
    # Count the number of digits in the current number
    num_digits = len(str(num))
    # Check if the number of digits is even
    if num_digits % 2 == 0:
        count += 1

# Print the count of numbers with an even number of digits
print(count)
