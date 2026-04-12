def isTriangle(sides):
    if sum(sides) == 0:
        return False
    else:
        a = sides[0] + sides[1] >= sides[2]
        b = sides[1] + sides[2] >= sides[0]
        c = sides[2] + sides[0] >= sides[1]
        return a and b and c


def equilateral(sides):
    return isTriangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return isTriangle(sides) and len(set(sides)) <= 2
    


def scalene(sides):
    return isTriangle(sides) and not isosceles(sides)
