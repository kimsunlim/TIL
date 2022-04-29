# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:58:24 2022


"""


#브루트포스 brute force
#완전탐색알고리즘, 모든 경우의 수를 탐색하면서 요구조건에 충족되는 결과만 가져옴
#예외없이 100%확률로 정답만 출력
#가장 간단한 알고리즘 스타투


#백준 2798 블랙잭

n,m=map(int,input().split())
arr=list(map(int,input().split())) #카드를 list화 하여 저장

result=0


for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]>m:
                continue
            
            else:
                result=max(result, arr[i]+arr[j]+arr[k])
                
print(result)
                
 
    
#인덱스를 유용하게 활용하자!





#백준 2231 분해합

n=int(input())
result=0

for i in range (1,n+1): #모든 경우의수 부루트포스
    a=list(map(int,str(i))) #각 i자리수 더함
    s= i + sum(a) #분해합 = 생성자+ 각자릿수 더함    
    if (s == n):  
        result=i
        break
    print(result)






#백준 7568 덩치

# 입력 받은 덩치의 정보를 리스트로저장
#고정된 하나의 인덱스를 둠
# 다른 인덱스를 리스트 전체로 돌리면서 조건문을 통해 덩치가 모두 큰경우에만 +1
#고정된 인덱스값 올림

N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for c in people : #0
    rank = 1 #1 
    
    for n in people:
        if (c[0]!=n[0]) & (c[1]!=n[1]): #2  
            if (c[0]<n[0]) & (c[1]<n[1]): #3 w, h 모두 큰 경우
                rank += 1
            
    print(rank)
        
        





#백준 1018 체스판

#흰색과 검은색이 공존하는 M*N크기의 보드에서
# 어떤 정사각형은 검은색, 나머지는 흰색으로 칠해져 있다.
# 이 보드를 잘라서 8*8 체스판을 만들려고 하는데
# 체스판은 체크무늬 형태로 칠해져있어야 한다.
# 보드에서 잘라냈을때, 바꿔서 칠해야 하는 색의 최소값을 구하라
# 체스판 색칠의 경우는 맨 왼쪽이 흰색인 경우, 검은색인 경우
# 두 가지 뿐이다.

# 생각
# 일단 전부 받아온다.
# N*M 판을 전체 경우의 수로 돌려야 한다.
# 그러기 위해서는 인덱스가 8을 넘지 않도록 조정을 해줘야 한다.
# 9*9에서 움직여서 조사할 수 있는 경우의 수는 2*2 4개이며,
# 10*10에서 움직여서 조사할 수 있는 경우의 수는 3*3 9개이고
# 11*11에서 움직여서 조사할 수 있는 경우의 수는 4*4 16개이다.
# 따라서, i는 N-7의 범위에서, j는 M-7의 범위에서 움직인다.
# 이후에 전체 경우의수를 다 돌면서
# W로 시작한 경우, B로 시작한 경우를 나누어서 판단한다.

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))
        





#백준 1436 영화감독 숌

n= int(input())
first=666  #666지정

#숫자를 1씩늘리면서 666이 포함되면 카운트하고 아니면 안함


#가능한 경우 다 돌려야하기에while구문
#하나씩 다 찾을땐while구문 사용

while n!=0:
    if '666' in str(first): #666이란 문자열이 문자열(first)안에 있으면
        n=n-1 #1감소
        if n == 0: #n=0이면
            break #탈출
        first = first+1 #first값 1증가  
    
        
print(first)
        
    







