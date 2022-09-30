# create a list if it is an integer reverse it else keep it as it is
# l = ["hi","hello",123,456]
#o/p ["hi","hello",321,654]
l = ["hi","hello",123,456]
l1 = []
for item in l:
    if isinstance(item,str):
        l1.append(item)
    else:
        item = (str(item))[::-1]
        l1.append(int(item))
print(l1)

# create a dictionary if the item is string, ikey - value pair item reversed string if it is amn int return the value of the lenngth of item

d = {}
for ele in l:
    if isinstance(ele,str):
        d[ele]= ele[::-1]
    else:
        d[ele] = len(str(len))
print(d)