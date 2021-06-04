#Python has a built-in function ‘map’ that applies a function to each element of a list.
#Provide an implementation for map using list comprehensions.
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(list(x))
