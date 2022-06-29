

#백준 1149 RGB거리 

#집을 칠하는 비용의 최솟값 출력 

#1번집 !=2번집
#N번집 != N-1번집
#i-1!=i!=i+1

#앞뒤로 있는 집과의 색은 같으면 안됨 


n=int(input()) #집의 수
dp=[] #집 리스트

for i in range(n):
    dp.append(list(map(int, input().split())))


for i in range(1,len(dp)):
    dp[i][0]= min(dp[i-1][1], dp[i-1][2])+dp[i][0] #빨강
    dp[i][1]= min(dp[i-1][0], dp[i-1][2])+dp[i][1] #초록
    dp[i][2]= min(dp[i-1][0], dp[i-1][1])+dp[i][2] #파랑
    
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2])) #  #3개의 값 중 가장 작은것

#풀이 
#min(dp[i-1][1], dp[i-1][2])+dp[i][0]
#dp[i][0] 기준으로 빨강색
#dp[i-1][1] 초록이고, dp[i-1][2]파랑으로 색칠될것인데 그 중 최솟값 추출