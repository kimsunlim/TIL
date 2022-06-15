
# 프로그래머스 LV.1 휴대폰번호가리기 

#1. 문자열 폰넘버
#2, 뒷자리 4개 제외
#3. 나머지는 *로 마스킹

def solution(s):
    return "*" *(len(s)-4)+s[-4:]

# 뒤의 4자릿수 빼고 *로 다 리턴한다음 (곱하기로 표현)

# 뒤의 4자리수 다시 표현 



##풀이2
def solution(s):
    for i in range(len(s)-4): #뒤의 4자리수만 빼기 
        s=s.replace(s[i],'*',1)
    return s