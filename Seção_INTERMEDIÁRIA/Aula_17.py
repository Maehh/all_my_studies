# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))


def generatoor(n=0, max=10) :
    yield 1     # Pausa
    print('Continuenado')

    yield 2     # Pausa

    print('Continuenado')
    yield 3     # Pausa
    
    print('Termino')
    return 'ACABO'

def generator(n=0, max=10) :
    while True :
        yield n
        n += 1
        if n > max :
            return 
        
gen = generator(5, 20)
print(next(gen))
print(next(gen))
print(next(gen))

for n in gen :
    print(n)

# yield from

def gen1() :
    print('COMEÇO GEN 1')
    yield 1
    yield 2
    yield 3
    print('ACABO GEN 1')


def gen2(gen=None) :
    print('COMEÇO GEN 2')
    if gen is not None :
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABO GEN 2')

def gen3() :
    print('COMEÇO GEN 3')
    yield 10
    yield 20
    yield 30
    
    print('ACABO GEN 3')

g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()

for p in g1 :
    print(p)
for p in g2 :
    print(p)
for p in g3 :
    print(p)
