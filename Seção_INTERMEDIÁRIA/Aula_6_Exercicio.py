def double_triple_quad(multiplier) :
    def action(num):
        return num*multiplier
    return action


dobro = double_triple_quad(2)
triplo = double_triple_quad(3)
quad = double_triple_quad(4)
quin = double_triple_quad(5)

print(dobro(12))
print(triplo(2))
print(quad(20))
print(quin(1))