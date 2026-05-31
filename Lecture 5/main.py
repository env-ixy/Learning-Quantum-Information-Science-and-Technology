import numpy 
ket0 = numpy.array([[1],
                    [0]])
bra1 = numpy.array([[0, 1]])
outer_product = ket0 @ bra1
print(outer_product)