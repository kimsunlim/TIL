 #프로그래머스 LV.1  나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    answer=[] #리스트생성
    
    for i in arr:
        if i%  divisor ==0:
            answer.append(i) #리스트에 넣을거면 append쓰기!! 명심!!
            
    answer.sort()
    
    if len(answer) ==0:
        answer.append(-1)
        
    return answer
        