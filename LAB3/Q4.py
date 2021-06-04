#Python has a built-in function ‘filter(f, a)’ that returns items of the list ‘a’ for which
#f(item) returns true. Provide an implementation for filter using list comprehensions
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)