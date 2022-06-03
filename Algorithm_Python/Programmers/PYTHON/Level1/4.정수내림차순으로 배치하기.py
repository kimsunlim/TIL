

# 프로그래머스 LV.1 정수 내림차순으로 배치하기

def solution(n):
     n=list(str(n)) #문자형으로 바꿔주고
     n.sort(reverse=True) #내림차순으로 정렬
     return int("".join(n)) #sting으로 join 변환해준뒤 int로 바꿔서 리턴
 
    
 
# .join() 은 리스트를 문자열로 일정하게 합쳐줌
#공백기준으로 리스트의 요소들을 스트링으로 바꿔반환한다는 소리임