# sum all the numbers in the below string
from curses.ascii import isdigit


s = "Sony12India567Pvt2ltd"
sum = 0
for ch in s:
    if ch.isdigit():
        sum = sum + int(ch)
print(sum)
