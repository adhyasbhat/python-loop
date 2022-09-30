# revese the string without using any inbuilt function
from errno import EHOSTDOWN
from operator import length_hint


s = "hello"
res = ""
for ch in s:
    res = ch + res #concantination 
print(res)
# trace 


'''res is empty 1st 
ch contains h so h will be added to res 
next ch + res here contantination takes place ie h is followed by e = eh
next l will be added so it will become leh'''