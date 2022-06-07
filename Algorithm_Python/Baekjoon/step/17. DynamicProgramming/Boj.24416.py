
#다이나믹 프로그래밍
#백준 24416 알고리즘수업- 파보타치수 1

#재귀 호출에 비해 동적 계획법이 얼마나 빠른지 확인



#피보나치 재귀 호출 코드
#fib(n) 
#   { if (n = 1 or n = 2)
#    then return 1;  # 코드1
#    else return (fib(n - 1) + fib(n - 2));}
   
   
#피보나치 동적프로그래밍

#fibonacci(n) {
#    f[1] <- f[2] <- 1;
#    for i <- 3 to n
#        f[i] <- f[i - 1] + f[i - 2];  # 코드2
#    return f[n];
#}


#코드1, 코드2 실행 횟수를 한줄에 출력


def fib(n):
    if n==1 or n ==2:
        return 1
    else:
        return fib(n-1) +fib(n-2)  #연산식 불러오는 방법
    
def fibonacci(n):
    dp=[0] * (n+1)
    dp[1],dp[2] =1,1    #1번과 2번이 각각 1이라는 설정
    cnt2=0 
    for i in range(3, n+1):   #3번부터 끝까지 앞의 두수를 더하는 방식임 ( 전 숫자와 전전숫자)
        cnt2+=1 
        dp[i]= dp[i-1]+dp[i-2]  #연산식을 불러오는게 아니라 dp[3]구하고, dp[4] 구하는 방식임 그래서 기존에 구한 dp[3]에 대한 결과를 가져오는것
    return cnt2 


n= int(input())
print(fib(n),fibonacci(n))









