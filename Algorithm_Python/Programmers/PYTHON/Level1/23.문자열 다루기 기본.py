# 프로그래머스 LV.1 문자열 다루기 기본



def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        answer=True
        
    else: 
        answer=False
        
    return answer

## isdigit  >> 문자를 검사해서 숫자인지 아닌지 검사해주는 메소드! 
#숫자일 경우 True  아닐경우 False 반환하도록 함