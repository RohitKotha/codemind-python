def maximum69Number(num):
    num_str = str(num)
    max_num = num

    for i in range(len(num_str)):
        if num_str[i] == '6':
            max_num = int(num_str[:i] + '9' + num_str[i+1:])
            break

    return max_num

# Example usage:
num = int(input())
result = maximum69Number(num)
print(result)
