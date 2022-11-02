def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2



def solution(sides):
    sides.sort()
    
    if sides[0]+sides[1] >sides[2]:
        return 2    
    else:
        return 1