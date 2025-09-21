count = 0
def greet():
  if count == 5:
    return
  count += 1
  greet()
  print("Devil")