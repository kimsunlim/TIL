# 프로그래머스 LV.1 x만틈 간격이 있는 n개의 숫자

#x부터 시작해 x씩 증가하는 숫자를 n개지니는 리스트 리턴

def solution(x,n):
    answer=[]
    for i in range(1,n+1):
        answer.append(x*i)
    return answer


#한줄에 코드를 못만들겠으면 리스트에 담아서 차례로 처리해주기!
