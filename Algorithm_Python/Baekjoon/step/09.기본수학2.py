# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:19:43 2022

@author: KMMD011
"""

#Q1. 소수찾기
#소수는 1과 자기자신으로만 나누어떨어짐

n=int(input())
data=list(map(int,input().split())) #문자열 받기
count=0

for x in data:
    for i in range(2,x+1):
        if x % i==0:
            if x==i:
                count+=1
                
            break
        
print(count)



#Q2. 소수
# input
M = int(input())
N = int(input())

# process
decimal = []
for i in range(M, N+1):
	for j in range(2, i+1):
		if j == i:
			decimal.append(i)
		if i % j == 0:
			break

# output
if not decimal:
	print(-1)
else:
	print(sum(decimal))
	print(decimal[0]) #인덱스로 가장 작은요소 추출
    
    
    
    
    
    
    
#Q3. 소인수분해
n=int(input())
    
#분해가 될때까지루프 돌리기
while n !=1:
    for i in range(2, n+1):
        #나눠지면 출력
        #다음을 위해 해당수로 n을 나눠줌
        
        if(n%i==0):
            print(i)
            n=n//i
            break
            
    
    
    
    
#Q4. 소수구하ㄱ기
    
x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1: #1은 소수가 아뉘지!
        continue
    for j in range(2, int(i** 0.5)+1 ):
        if i%j==0:
            break
    else:
        print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    