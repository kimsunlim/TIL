# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:25:54 2022

@author: KMMD011
"""

#Q1 손익분기점

#A는 고정비, B는 변동비, C는 노트북가격
#수입이 총비용(고정+변동)보다 많아지는 손익분기 시점 
#손익분기가 없으면 -1
#판매량을 n이라고하면, C*n= (A+B)*N  >> n=A/(c-b)

A, B, C= map(int,input().split())

#손익분기가 존재하지않을때
if B>=C: #변동비용이 노트북 가격보다 높을때, 수익창출X
    print(-1)
    
#손익분기 존재
else:
    print(A//(C-B)+1)
    
    
#A/(c-b)는 손익분기점일때이고 이익이 발생할때는 +1할때이다.








#Q2. 벌집

#힌트를 찾는 연습을 먼저하자!!!
#방 1개 지나가는 숫자 6개 방2개 12, 방3개 18, 6씩 증가하는 모습!!
n=int(input())

cnt=1 #초기값 1!
cnt_six=6 #6씩증가하는 변수
count=1

while n>cnt:
    count+=1 #카운트 증가
    cnt+=cnt_six #초기값에 6증가
    cnt+=6 #그다음 cnt+_six는 6증가 장치까지 만들어줘야함!
print(count)




#Q3.분수찾기
#1/1 ->      1/2 -> 2/1 ->      3/1 -> 2/2 -> 1/3,,  1개 2개 3개 이런식으로 n개씩 늘어난다고 친다면
#홀수씩 늘어날 때는 분자는 n부터 1까지 줄어들고 분모는 1부터 n까지 늘어난다.
#짝수씩 늘어날 때는 분자는 1부터 n까지 늘어나고 분모는 n부터 1까지 줄어든다.


x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")
    




#Q4.달팽이는 올라가고싶다

import math

a,b,v =map(int,input().split())

solution= math.ceil((v-b)/(a-b))
print(solution)

# 나무높이 v에서 정상에 도달한 후 미끄러지지 않는 b를빼면 매일 (a-b)만큼 올라가고 있다.
# 달팽이는 (v-b)/(a-b)일동안 올라가게된다
#마지막날은 조금만 올라도 하루가 지난거여서, 소숫점이 나오면ceil로 올림해야한다.






#Q5. ACM호텔

T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 

    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)
    



#Q6. 부녀회장이 될테야

import sys

read = lambda: sys.stdin.readline().rstrip()

T = int(read())

for _ in range(T):
    floor = int(read())
    num = int(read())

    f_list = [i for i in range(1, num+1)]

    for i in range(floor):
        for j in range(1, num):
            f_list[j] += f_list[j-1]

    print(f_list[-1])



#Q7. 설탕배달


sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)





#Q8. 큰수 A+B



a,b= map(int, input().split( )) 

print(a+b)
















#컴파일 에러: 소스코드의 문법적 오류(프로그램 실행전),:를 안붙였다거나 for구문이 문법적으로 틀린경우 등
#런타임에러: 프로그램 실행중 발생한 오류 ,설계미스등