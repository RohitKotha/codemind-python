def isUniqueNumber(num):
    digits = str(num)
    digit_set = set(digits)
    
    if len(digits) == len(digit_set):
        return True
    else:
        return False

# Main program
num = int(input())

if isUniqueNumber(num):
    print("Unique Number")
else:
    print("Not Unique Number")
