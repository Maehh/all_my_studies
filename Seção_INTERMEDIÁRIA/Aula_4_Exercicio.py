
def multi(*args):
    count = 1
    for i in args :
        count *= i
    return count

test = multi(1, 2, 3, 4, 5, 6, 7)
print(test)

def oddpar(x):
    return x % 2 == 0

num = oddpar(348)

if num :
    print('Par')
else :
    print('Impar')