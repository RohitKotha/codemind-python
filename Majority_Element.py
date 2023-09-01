n = int(input())
arr = list(map(int, input().split()))
element_count = {}

for num in arr:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

for num, count in element_count.items():
    if count > n // 2:
        print(num)
        break
