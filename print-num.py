# print all the numbers in the below list

from curses.ascii import isdigit


l = ['abc','123','hello','23']
# for item in l:
#     if item.isdigit():
#         print(item)

l1 = []
for item in l:
    if item.isdigit():
        l1.append(item)
print(l1)