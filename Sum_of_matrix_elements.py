# Input the order of the 2-D array
M = int(input())
N = int(input())

# Initialize a 2-D array to store the elements
arr = []

# Input the elements into the 2-D array
for _ in range(M):
    row = list(map(int, input().split()))
    arr.append(row)

# Calculate the sum of all elements in the 2-D array
sum = 0
for i in range(M):
    for j in range(N):
        sum += arr[i][j]

# Output the sum
print(sum)
