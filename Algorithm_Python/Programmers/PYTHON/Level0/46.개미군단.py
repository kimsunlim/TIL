#개미군단
#https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    first=hp//5
    second=(hp-first*5)//3
    third=(hp-first*5-second*3)
    return first+second+third


###다른 풀이
def solution(hp):
    return hp//5+(hp%5//3)+((hp%5)%3)



