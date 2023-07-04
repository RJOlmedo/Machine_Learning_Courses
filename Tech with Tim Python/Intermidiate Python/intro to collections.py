from collections import Counter

#c = Counter('gallad')
#print(c)
#c = Counter([1, 2, 3, 4, 5])
#print(c)
#c = Counter(cats=4, dogs=7)
#print(c["cats"])

#print(list(c.elements()))

#print(c.most_common())

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'c', 'b']
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)