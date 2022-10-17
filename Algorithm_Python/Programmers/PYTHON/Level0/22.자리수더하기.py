def solution(n):
    answer=0
    while n:

        answer+=n%10
        n//=10
    return answer 



######

def solution(n):
    answer=0
    for i in str(n): #자료형으로 자릿수 출력
        answer+=int(n) #누적으로 합계 ,n는 자료형이라 int형으로 더해야함
    return answer

