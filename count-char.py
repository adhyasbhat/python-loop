# print the num of occurance of char in a string without inbuilt function

s = "hello world"
d ={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i] = d[i]+1
print(d)