li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x

#print(list(map(func, li)))
print([func(x) for x in li if x%2 == 0])

#new_list = []
#for x in li:
#    new_list.append(func(x))

#print(new_list)