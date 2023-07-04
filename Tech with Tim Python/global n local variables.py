var = 9
loop = True
newVar = 23

def func(x):
    global loop

    loop = 7

    if x == 5:
        return True
    
def otherFunc():
    newVar = 5
    print(newVar)

otherFunc()

loop = False
print(loop)