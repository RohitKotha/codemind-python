# Input the length of the array and the array of digits
N = int(input())
digits = list(map(int, input().split()))

# Start by adding 1 to the least significant digit
carry = 1

# Iterate through the digits in reverse order (from least significant to most significant)
for i in range(N - 1, -1, -1):
    total = digits[i] + carry
    digits[i] = total % 10
    carry = total // 10

# If there's a carry left, insert it as the most significant digit
if carry > 0:
    digits.insert(0, carry)

# Print the updated array of digits
print(*digits)
