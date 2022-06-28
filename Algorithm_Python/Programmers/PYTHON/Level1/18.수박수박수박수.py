# 프로그래머스 LV.1  수박수박수박수

##짝수일때 '수'출력
# 홀수일때 '박'출력
# 한곳에 담아줄것 

def solution(n):
    answer=''   #이곳에 넣어줄것 

    
    for i in range(n):
        if i %2 ==0:
            answer+='수'
        else:
            answer+='박'
            
    return answer
