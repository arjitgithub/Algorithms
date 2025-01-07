def lcm_of_array(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        num1 = lcm
        num2 = arr[i]
        gcd = 1
        # Finding GCD using Euclidean algorithm
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        gcd = num1
        lcm = (lcm * arr[i]) // gcd
    return lcm


# Example usage
arr1 = [1, 2, 8, 3]
arr2 = [2, 7, 3, 9, 4]
print(lcm_of_array(arr1))  # Output: 24
print(lcm_of_array(arr2))  # Output: 252