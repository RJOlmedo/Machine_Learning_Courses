def add7(x):
    return x+7

def is_odd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#b = list(filter(is_odd, a))
c = list(map(add7, filter(is_odd, a)))

print(a)
print(c)