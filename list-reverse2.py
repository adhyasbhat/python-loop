#write a program to reverse the list as below
#words = ['hi','hello','python']
# o/p ['nohtyp','olleh','ih']
words = ['hi','hello','python']
l = []
for item in words[::-1]:
    l.append(item[::-1])
print(l)