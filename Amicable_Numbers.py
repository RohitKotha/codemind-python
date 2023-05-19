def sum_of_divisors(num):
    # Calculate the sum of proper divisors of the given number
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    return div_sum

def isAmicable(num1, num2):
    # Check if the pair of numbers is Amicable
    sum1 = sum_of_divisors(num1)
    sum2 = sum_of_divisors(num2)
    
    if sum1 == num2 and sum2 == num1:
        return True
    else:
        return False

# Main program
num1 = int(input())
num2 = int(input())

if isAmicable(num1, num2):
    print("Amicable")
else:
    print("Not Amicable")
