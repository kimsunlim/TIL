

# 프로그래머스 LV.1  정수 제곱근 판별
# n이 어떤 양의 정수 x의 제곱인지 아닌지 판단

#n이 양의정수 x제곱이라면 x+1제곱근 리턴
#n이 양의 정수 x제곱근이 아니라면 -1 리턴


def solution(n):
    a= n **0.5  ##제곱근 변수 지정
    if int(a) ==a:
        return (a+1) **2 
    else:
        return -1
    

