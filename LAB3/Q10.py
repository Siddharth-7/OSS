#Write a program to find anagrams in a given list of words. Two words are called
#anagrams if one word can be formed by rearranging letters of another. For example
#‘eat’, ‘ate’ and ‘tea’ are anagrams.

def areAnagram(str1, str2):

    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0

    return 1

str1 = "eat"
str2 = "tea"

if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")



