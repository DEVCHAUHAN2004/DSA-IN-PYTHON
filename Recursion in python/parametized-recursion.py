def func(sum, i, n):
    if i > n:   # base case
        print(sum)
        return
    func(sum + i, i + 1, n)   # recursive call

# call
func(0, 1, 10)
#  55