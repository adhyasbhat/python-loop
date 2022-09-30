# in given list if the 1st char in tat item starts with vowel then print that item
l = ["apple","mocrosoft","facebook","instagram"]
for item in l:
    if item[0] in "aeiouAEIOU":
        print(item)

# in the given list print the items which has even len

l = ["cat",'ball']
for item in l:
    if len(item)%2==0:
        print(item)