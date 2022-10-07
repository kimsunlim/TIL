def solution(n):

    answer=0  #숫자를 담아줄 저장 공간
    for i in range(2,n+1,2):
        answer+=i
    return answer
