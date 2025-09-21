count = 0
def greet():
  if count == 5:
    return
  print("Devil")
  count += 1
  greet()
  