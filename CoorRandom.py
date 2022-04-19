import random as ra

def RandomCoord(x1,x2,y1,y2):
    x = ra.randint(x1,x2)
    y = ra.randint(y1,y2)
    return x, y

coor = RandomCoord(-8,-4,-7,10)
print(coor)
#print(coor[0])
#print(coor[1])