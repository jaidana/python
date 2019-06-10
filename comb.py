n = [(x,y) for x in [3,1,2] for y in [2,1,3] if x != y] 

# another exercice, filter the negative values
vec = [-4,-3,-2,1,2,3]
m = [x for x in vec if x >= 0]
# abs changes negative inte positive (absoult)
n = [abs(x) for x in vec]

#create a list of tuples (number, cube)
c = [(x, x**3) for x in range(6)]
# tuple should be parenthesized

# flatten a list
vec =[[1,2,3],[4,5,6],[7,8,9]]
f = [num for elem in vec for num in elem]
# [[]] list ensemble s'apple element 
