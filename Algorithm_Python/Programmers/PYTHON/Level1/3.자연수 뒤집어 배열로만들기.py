


# 프로그래머스 LV.1 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열형태로 리턴하기
#12345 > [5,4,3,2,1]




#첫번째 내가 푼 코드

def solution(n):
    a =list(map(int,str(n)))
    a.sort(reverse=True)
    return a


#코드 실행에서는 통과였으나 제출하기를 누르니 정확성 테스트를 통과히지 못함


def solution(n):
    a =list(map(int,str(n)))
    a.reverse()
    return a

#sort을 빼고 reverse 함수만 썼더니 통과

def solution(n):
    a = list(map(int,reversed(str(n))))
    return a


#reversed를 str(n)앞에 작성하니 정확성테스트 통과



##reverse 와 reversed 차이

#reverse >> list타입을 뒤집어줌, list에서 제공하는 함수
#reversed >> list에서 제공하는 함수가 아님! >str 반환

