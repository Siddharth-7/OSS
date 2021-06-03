#Write a function “lensort” to sort a list of strings based on length.
def lensort(list1):
    list1.sort(key=len)
    print(list1)

lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
lensort(lst)


