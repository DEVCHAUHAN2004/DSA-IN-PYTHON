n = int(input("Enter the number: "))
num = n
total = 0
nod = len(str(n))   # number of digits

if num < 0:
    print("Not a valid number")
else:
    while num > 0:
        digit = num % 10               # last digit nikalo
        total = total + (digit ** nod) # digit^nod add karo
        num = num // 10                # last digit hatao

    if n == total:
        print("Armstrong")
    else:
        print("Not Armstrong")
