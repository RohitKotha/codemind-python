def isPerfectSquare(num):
    squareRoot = int(num ** 0.5)
    return squareRoot * squareRoot == num

num = int(input())

if isPerfectSquare(num):
    print("True")
else:
    print("False")
