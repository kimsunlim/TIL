# 프로그래머스 LV.1  짝수와홀수



def solution(num):
    answer='' #결과값을 넣을 변수 지정
    
    if (num %2 ==1):   #2로 나눠서 나머지가 1인경우 홀수 //반대로 0인경우는 짝수
        answer ='Odd'
    else:
        answer = 'Even'
    
    return answer



#아직 변수 지정이 해깔린다 
#변수만 잘 만들어줘도 깔끔하고 수월하게 문제가 풀릴 것 같다!! 화팅
