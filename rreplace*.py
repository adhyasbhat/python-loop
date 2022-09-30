# replace all the character with occurance more than once with * in the string hello world
from dataclasses import replace
from re import I


s = "apple"
l = ""
for ch in s:
    if s.count(ch)>1:
        l = l+ "*"
    else:
        l = l+ch
print(l)









   