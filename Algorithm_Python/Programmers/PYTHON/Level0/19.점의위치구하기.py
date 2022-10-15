def solution(dot):
    answer = 0
    for i in dot:
        if dot[0]>0 and dot[1]>0:
            return 1
        elif dot[0]<0 and dot[1]>0:
            return 2
        elif dot[0]<0 and dot[1]<0:
            return 3
        elif dot[0]>0 and dot[1]<0:
            return 4
    