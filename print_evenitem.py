# print elements presemt in even index
# with using enumerate 
iterable = ["apple","google","walmart","flipkart","gamil"]

for index, item in enumerate(iterable):
    if (index%2==0):
        print(item)

# without using enumerate
for elements in iterable[::2]:
     print(elements)
# -------------------------OR-------------------------
for i in range(len(iterable)):
    if i%2 == 0:
        print(iterable[i])