def isAutomorphic(num):
    square = num ** 2
    num_str = str(num)
    square_str = str(square)
    
    if square_str.endswith(num_str):
        return True
    else:
        return False

# Main program
num = int(input())

if isAutomorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
