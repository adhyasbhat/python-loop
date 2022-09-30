from collections import defaultdict
l = ["apple","google","gamil","apple","gamil","flipkart","apple"]
d = {}
dd = defaultdict(list)
for index,word in enumerate(l):
    dd[word] += [index]
print(dd)