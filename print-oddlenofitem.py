# create dictionary of index and elememts pair where elements must be of odd length --- for liven list below it should print apple walmart gmail with their index

l = ["apple","google","walmart","flipkart","gmail"]
d = {}
for index, ele in enumerate(l):
    if len(ele)%2==1:
        d[index] = ele
print(d)