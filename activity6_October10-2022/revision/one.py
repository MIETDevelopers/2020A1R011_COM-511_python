d1 = {1: 10}
d2 = {2: 20}
d3 = {3 : 30}
d4 = {}
#dict4 = dict(dict1.items() + dict2.items() +dict3.items())
#d4  = dict(d1, **d2)
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)