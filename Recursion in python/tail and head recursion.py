# 1. Head Recursion

# In head recursion, the recursive call happens first, and then the current statement (like print) is executed after returning from recursion.

# def head_recursion(i, n):
#     if i > n:
#         return
#     head_recursion(i + 1, n)  # recursive call first
#     print(i)                  # action after recursion

# head_recursion(1, 4)


# Output:

# 4
# 3
# 2
# 1


# ✅ Notice that numbers are printed in reverse order because the action happens after the recursion returns.

# 2. Tail Recursion

# In tail recursion, the action happens first, and then the recursive call is the last thing executed.

# def tail_recursion(i, n):
#     if i > n:
#         return
#     print(i)                  # action first
#     tail_recursion(i + 1, n)  # recursive call last

# tail_recursion(1, 4)


# Output:

# 1
# 2
# 3
# 4