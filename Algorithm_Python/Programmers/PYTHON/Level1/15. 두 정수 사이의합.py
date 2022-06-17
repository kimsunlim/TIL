# 프로그래머스 LV.1 두 정수 사이의 합

#a~b사이 합구하기
#두 수는 대소관계 없음



def solution(a,b):
    if a<b:  # 대소관계가 어려워서 파악하기 힘들때 지정
        return sum(list(range (a,b+1))) #b가 더클 때 a부터 돌아서 합계산
    else:
        return sum(list(range(b,a+1))) #그게 아닐때 b부터 합 계산
    
    #차근히 하면 간결하게 코딩할수 있다!!홧팅
    
