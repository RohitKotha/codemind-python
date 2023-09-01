n = int(input())
candies = list(map(int, input().split()))
extraCandies = int(input())

max_candies = max(candies)
result = []

for candy_count in candies:
    result.append(candy_count + extraCandies >= max_candies)

print(*result)
