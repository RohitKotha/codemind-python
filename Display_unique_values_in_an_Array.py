# Input the size of the array
n = int(input())
# Input the array elements as a list
arr = list(map(int, input().split()))

# Create a dictionary to store the frequency of each element
element_freq = {}

# Count the frequency of each element in the array
for num in arr:
    if num in element_freq:
        element_freq[num] += 1
    else:
        element_freq[num] = 1

# Find and display the unique elements
unique_elements = []
for key, value in element_freq.items():
    if value == 1:
        unique_elements.append(key)

# If there are no unique elements, print -1
if len(unique_elements) == 0:
    print(-1)
else:
    # Print the unique elements separated by space
    print(" ".join(map(str, unique_elements)))
