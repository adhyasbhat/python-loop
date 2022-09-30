# extract each character in string

s = "hello"
d = {}
i =0

while i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]]+=1
    i+=1
print(d)

#----------------------------------------or-------------------------
while i in range(len(s)):
    d[s[i]] = s.count(s[i])
    i+=1
print(d)

# iterating over a string in reversed direction

s="hello world"
print(s[::-1])
#---------------------OR------------------------

s = "hello world"
print(len(s))
i = len(s)-1

while i in range(len(s)):
    print(s[i])
    i-=1

#extract each character n print it with its index

s = "hello"
for i in range (len(s)):
    print(s[i],i)