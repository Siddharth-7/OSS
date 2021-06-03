#Write a function group (list, size) that take a list and splits into smaller lists of given size.
def group(l,size):
    for i in range(0,len(l), size):
        yield l[i:i+size]
l=[1,2,4,5,6,9,0,34,56,89,31,42]
x=list(group(l,3))
print(x)


