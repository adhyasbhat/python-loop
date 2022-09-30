names = ['apple','mango','banana','strawberry']
l = []
for item in names:
    if len(item)%2 == 0:
        l.append(item)
print(l)