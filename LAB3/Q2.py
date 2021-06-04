#Write a program wrap.py that takes filename and number of characters per line (width)
#as arguments. The program must wrap the lines of the file longer than entered width.
import textwrap

value = """Summer has come and passed The innocent can never last
Wake me up when September ends Like my fathers come to pass
Seven years has gone so fast Wake me up when September ends
Here comes the rain again Falling from the stars
Drenched in my pain again Becoming who we are"""

wrapper = textwrap.TextWrapper(width=20)

word_list = wrapper.wrap(text=value)

for element in word_list:
    print(element)