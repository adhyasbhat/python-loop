# print factorial of given number

num = int(input())
fact = 1
for i in range (1,num):
    fact = fact*i
print(fact)

# print factorial for given range
l = []
fact = 1
for i in range(1,6):
    fact = fact*i
    l.append(fact)
print(l)