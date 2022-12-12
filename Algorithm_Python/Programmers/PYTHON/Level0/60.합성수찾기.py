#https://school.programmers.co.kr/learn/courses/30/lessons/120846#
##합성수 찾기 >> 3개이상의 약수를 가진 숫자 찾기

def solution(n):
    answer=[]
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
            if count>=3:
                answer.append(i)
                break
    return len(answer)

