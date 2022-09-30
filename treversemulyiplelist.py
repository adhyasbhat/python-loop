# traveshing through multiple lists and creating a dictionary
l1 = [10,20,30]
l2 = ["apple","google","flipkart"]
d = {}
for i in range(len(l1)):
    d[l2[i]] = l1[i]
print(d)

for key,value in zip(l2,l1):
    d[key]=value
print(d)