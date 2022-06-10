
##백준 9461 파도반 수열
#피보나치 수와 비슷한 규칙을 찾아 동적계획법으로 품


# 1 1 1 2 2 3 4 5 7 9

#i=1일때, i번째 숫자와 i+1번째 숫자를 더한값이 i+3에 놓임
#이 패턴을 주목해야함


wh=[0 for i in range(101)]

wh[1]=1
wh[2]=1
wh[3]=1


##DP쓰기 
for i in range(0,98):
    wh[i+ 3]= wh[i]+wh[i+1]
    
t= int(input())
for i in range(t):
    n=int(input())
    print(wh[n])