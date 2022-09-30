#zip -zip(*iterable)
from itertools import zip_longest


l = ['hi','hello','welcome','python']
l1 = [1,2,3,4]
res = zip(l,l1)
print(list(res))
#o/p [('hi',1),('hello',2),('welcome',3),('python',4)]

# zip_longest - used when num of items in list is diff
l = ['hi','hello','welcome','python','programming']
l1 = [1,2,3,4]
res = zip_longest(l,l1)
print(list(res))
#---------------------------or---------------------
l = ['hi','hello','welcome','python']
l1 = [1,2,3,4,5]
res = zip_longest(l,l1)
print(list(res))

l = ['hi','hello','welcome','python']
l1 = [4,2,1,5] 
res = zip(l1,l)
res1 = sorted(res)
print(res1)

# l = ['hi','hello','welcome','python']
# l1 = [4,2,1,5] 
# res = zip(l1,l)
# res1 = sorted(res)
# print(res1)

l = ['hi','hello','welcome','python']
l1 = [4,2,1,5] 
dic = {}

for i in range(len(l1))
    dic[l[i]] = l1[i]

res = zip(l1,l)
res1 = sorted(res)
print(res1)
