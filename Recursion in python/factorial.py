def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n+1):
        fact *= i
    return fact

n = int(input("Enter the number: "))
print("Factorial:", factorial(n))

