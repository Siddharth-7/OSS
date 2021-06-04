#Write a program to count frequency of characters in a paragraph.
from collections import Counter


test_str = "Summer has come and passed the innocent can never last Wake me up when September ends"

res = Counter(test_str)

print("Count of all characters in paragraph is :\n "
      + str(res))