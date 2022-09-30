#write a program to find its palandrome or not without reversed method
s = "madam"
res = ""
for ch in s:
        res = ch + res
if res == s:
    print("palandrome")
else:
    print("not palandrome")

# using reversed method
if s == "".join(list(reversed(s))):
    print("palandrome")
else:
    print("not palandrome")