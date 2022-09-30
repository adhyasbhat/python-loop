#creating dictionary of city and population pairs using dict comprehension

cities = ['tokyo','delhi','shanghai','sao paulo','mubai']
population = ['32','12','43','42','87']

d = {}
d = zip(cities,population)
print(dict(d))

print(dict(zip(cities,population)))