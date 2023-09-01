# Input the number of integers
n = int(input())

# Input the array of integers
nums = list(map(int, input().split()))

# Create a set to store the top three maximum values
top3 = set()

# Iterate through the array
for num in nums:
    top3.add(num)
    if len(top3) > 3:
        top3.remove(min(top3))

# If the third maximum doesn't exist, return the maximum
if len(top3) < 3:
    print(max(top3))
else:
    print(min(top3))
