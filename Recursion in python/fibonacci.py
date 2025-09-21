def fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)

    for i in range(2, n):   # 0 aur 1 already print kar diye
        c = a + b
        print(c)
        a = b
        b = c

fibonacci(5)

# 0
# 1
# 1
# 2
# 3
