# 프로그래머스 LV.1 문자열 내림차순

# sort 문제
#문자열은 join 써서 합쳐야함!!

def solution(s):
    n=list(s)# 리스트형으로 변환
    n.sort(reverse=True) #내림차순 
    return ''.join(n) #문자열 join으로 꼭 합치기!