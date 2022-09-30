#built a list of tuples with string and its length pair

from ast import keyword
from unittest import result


l = ["adhya","pranit","gube"]
l1 = []

for ele in l:
    l1.append((ele,len(ele)))
print(l1)
#------------------------or--------------------------
print([(ele,len(ele)) for ele in l])

#take a list of string and reverse the string if the string is of odd length, otherwise keep it as is

s = "pranit is biggest gube"
l = s.split()
l2 = []
for ele in l:
    if len(ele)%2==1:
        l2.append(ele[::-1])
    else:
        l2.append(ele)
print(l2)
#-------------------------or-------------------
print([ele[::-1]if len(ele)%2==1 else ele for ele in l])

#flippping keys and values of the dictiory using dict comprehension
dict = {"name":1,"adhya":2,"abhinav":3}
d = {}
for key, value in dict.items():
    d[value] = key
print(dict)
#---------------------------or--------------------------
print({value:key for key, value in dict.items()})

d = {"name":1,"adhya":2,"abhinav":3}
print({key:value[::-1] if isinstance(value,str) else value for key,value in d.items})