#enumerate will give index 
l = [1,2,3,4]
for index, item in enumerate(l):
    print(index,item)

#--------------------------------

d = {'a':1,'b':2,'c':3,'a':4}
# o/p {'a':[1,4],'b':2,'c':3}
d1 = {}
for index, key, value in enumerate(d):
    if key not in d1:
        d[key] = [index]
    else:
        d1[key].append[index]
print(d1)

#------------------------------------------
for key, value in enumerate(d):
    if key not in d1:
        d[key] = 1
    else:
        d1[key]+=1
print(d1)