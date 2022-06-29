# 프로그래머스 LV.1  서울에서 김서방찾기

#string 형 배열에서 특정 문자를 찾는 문제이며, 출력할때 int형을 str형으로 변환



def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=='Kim':
            answer=i
        
        
    return ('김서방은 '+str(answer)+'에 있다')