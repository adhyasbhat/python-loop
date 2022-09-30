l = ['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt']
d = {}
for item in l:
    file,extension = item.split(".")
    if extension not in d:
        d[extension] = [file]
    else:
        d[extension]+=[file]
print(d)
