#https://school.programmers.co.kr/learn/courses/30/lessons/42748
#k번째수

def solution(array,commands):
    answer=[]
    for i in commands:
        ary=array[i[0]-1:i[1]]
        ary.sort()
        answer.append(ary[i[2]-1])
    return answer

