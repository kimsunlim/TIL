
# 백준 1904 01타일
# 점화식 값을 특정 상수로 나눈 나머지를 구하는 문제

#n=1  :  1
#n=2  : 00
# n=3 : 1 0 0 , 111 
# d[n] = d[n-2] + d[n-1]




import sys 
input= sys.stdin.readline 


n= int(input())
dp=[0]*1000001  #0인덱스 사용 노노
dp[1]=1   #1개인거 확정
dp[2]=2   #2개인거 확정

for k in range(3, n+1): #3  부터 경우의 수 돌리기
    dp[k]= (dp[k-1]+dp[k-2])%15746 ##출력이 커서 15746 나눔 #2진수열의 개수
print(dp[n])

#인덱스를 가져옴으로써 저장한 값 가져오는 것
#DP활용


#굳이 1부터 시작안해도 되고 특정 패턴이 있는 순서부터 힌트를 찾으면됨다 
