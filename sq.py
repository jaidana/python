squares = []
for x in range(20):
    squares.append(x**2)

#another methode
square = [x**2 for x in range(10)]

from math import pi
r = [abs(round(pi,i)) for i in range(6)]
# change abs with int str possible

#matrix
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mr = [[row[i] for row in matrix] for i in range(3)]
mc = [[coloum[i] for coloum in matrix] for i in range(3)]
#transposed with append is also possible evry long

#it is a try
prime = [x for i in range(10) if i%2 ==0]
# prime

