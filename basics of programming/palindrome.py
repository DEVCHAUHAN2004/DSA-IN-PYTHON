n = int(input("Enter the number: "))
num = n
reverse = 0

if num < 0:
    print("Not a valid number")
else:
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if n == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")



# n = input("Enter the number: ")

# if n == n[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
