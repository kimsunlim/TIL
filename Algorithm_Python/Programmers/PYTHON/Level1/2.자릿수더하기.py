


# 프로그래머스 LV.1 자릿수 더하기
# 자연수 N의 각 자릿수의 합 구하기

def solution(n):
    s=list(map(int,str(n)))  #n을 문자열로 바꿔서 list에 담고 각 자릿수의 합을 구할수 있음
    return sum(s)




#내가 생각했던 방식은 코드가 길고 깔끔하지 않았음.
#다른 풀이 보면서 참고하기


def solution(n):
    answer=0
    
    for i in str(n):  #문자열로 바꿔서 나눠주고
            answer+=int(i) #하나하나 다시 더해주기!
    return answer