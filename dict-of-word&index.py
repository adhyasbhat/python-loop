from collections import defaultdict
# create a dict of word and its index pair
d = {} # d = dict()
l = ["apple","google","gamil","apple","gamil","flipkart","apple"]
for index,word in enumerate(l):
    if word not in d:
        d[word] = [index] # if index is not made list ([index]) then it will add the index -- apple will have 9 and not 0 3 6 ie it will add 0+3+6 
    else:
        d[word] = d[word]+[index] 
        #or d[word] = append[index]
print(d)

# using default dictionary
dd = defaultdict(list)
for index,word in enumerate(l):
    dd[word] += [index]
print(dd)