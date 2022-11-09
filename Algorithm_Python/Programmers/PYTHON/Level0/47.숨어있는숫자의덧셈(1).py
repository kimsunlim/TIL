# https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    answer=0
    for i in my_string:
        if i.isnumeric(): # 문자열이 숫자로 구성되어 있는지 판별 isdigit도 있음
            answer+=int(i) #int형태인 것만 덧셈
    return answer