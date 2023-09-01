N = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(N):
    count = 0
    for j in range(N):
        if i != j and nums[j] < nums[i]:
            count += 1
    result.append(count)

print(" ".join(map(str, result)))
