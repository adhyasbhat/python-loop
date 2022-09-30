# reverse the value in the dict if the value is string

d = {'a':'hello','b':100,'c':10.1,'d':'world'}
for key,value in d.items():
    if isinstance(value,str):
        d[key] = value[::-1]
    else:
        d[key]=value
print(d)