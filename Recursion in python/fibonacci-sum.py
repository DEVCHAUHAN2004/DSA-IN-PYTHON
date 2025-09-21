def fibonacci(n):
    a, b = 0, 1
    total = a + b   # sum of first two numbers

    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        total += c   # add each new term to sum
        a, b = b, c

    print("Sum:", total)

fibonacci(5)
