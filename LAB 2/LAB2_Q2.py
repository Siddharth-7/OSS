#Write a function “duplicate” to find all duplicates in the list.

def Duplicate(string):

    duplicates = []
    for char in string:

        if string.count(char) > 1:
            if char not in duplicates:
                duplicates.append(char)
    print(*duplicates)

s = "siddharth"
Duplicate(s)