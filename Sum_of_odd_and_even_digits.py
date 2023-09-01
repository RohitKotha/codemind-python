# Input the length of the array
n = int(input())

# Input the array elements as a list of integers
arr = list(map(int, input().split()))

# Initialize variables to store the sum of odd and even indexed digits
sum_odd = 0
sum_even = 0

# Iterate through the elements and calculate the sums
for i in range(n):
    if i % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

# Check if the difference is zero and print the result
if sum_odd - sum_even == 0:
    print("YES")
else:
    print("NO")
