# print 0 to 4

#while loop
i = 0
while i<5:
    print(i) 
    i+=1

#range
print(list(range(0,4)))

#------------------------------------------------------------------------------

s = "hello world"
i = 0
while i in range(len(s)):
    print(s[i])
    i+=1