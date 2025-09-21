def fibonacci_recursion(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

print(fibonacci_recursion(10))  # Output: 55
