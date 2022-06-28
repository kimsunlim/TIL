# 프로그래머스 LV.1  소수찾기 

# 1~n까지 숫자 사이에서 소수의 개수를 반환하는 함수를 만들어보라


def solution(n):
    answer =set(range(2,n+1))  #중복 제거 자료형에 2~n넣기
    
    for i in range(2, n+1):
        if i in answer:
            answer -=set(range (i*2, n+1, i))  #i의 한 배수 큰 숫자부터 n+1까지 범위를 공차가i인거 빼기
    return len(answer)  # 즉 i의 배수인거 다 빼는 코드임!! 그러면 소수만 남음



#에라스토테네스체
#소수판별 알고리즘 , 소수를 대량으로 빠르고 정확하게 구하는 방법! 
# 배열을 할당하여 해당하는 값을 넣어주고 이후 하나씩 지워나가는 원리임 

                   