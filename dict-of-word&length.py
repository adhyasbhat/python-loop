# create a dict of word and its length pair
d = {} # d = dict()
l = ["apple","google","flipkart"]
for ele in l:
    d[ele] = len(ele)
print(d)

# create a list of tuple having its word n length pair
l = ["apple","google","flipkart"]
l1 = [] # l1 = list()
for ele in l:
    l1.append((ele,len(ele)))
print(l1)