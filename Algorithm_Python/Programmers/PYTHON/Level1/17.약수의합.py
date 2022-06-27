

# 프로그래머스 LV.1  약수의합 

def solution(s):
    answer=0
    for i in range(1,s+1):
        if s%i ==0:
            answer+=i
    return answer 


#나머지0이 되는 약수들을 다 더함
