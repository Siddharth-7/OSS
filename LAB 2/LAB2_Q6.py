#Use Python Built-in Functions ‘open’, ‘read’, ‘’readline, ‘write’,’writeline’ to work with
#files.
f = open("file.txt", 'w')
f.write("siddharth \nsharma\n")

f.close()
f = open("file.txt", 'r')
print(f.readline())
print(f.read())
f.close()