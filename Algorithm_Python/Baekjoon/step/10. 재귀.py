# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:15:58 2022

@author: KMMD011
"""


##재귀함수: 자신을 정의할떄 자기 자신을 재참조
#주로 반복문으로 구현


#1. 팩토리얼

n= int(input())

result=1
if n>0:
    for i in range(1,n+1):
        result*=i  ##result에 담는다 result가 1이니깐 곱하면 그 수가 나옴
print(result)



    
#2. 파보나치수 5

n=int(input())

fabo =[0,1] #0,1먼저 담기
for i in range(2,n+1): #2부터 루프돌기
    num =fabo[i-1]+fabo[i-2] #각각 리스트 끝자리의 두개 반환
    fabo.append(num) #리스트에 어팬드하기!!
    
print(fabo[n])



#3. 별찍기-10


def draw_stars(n):
  if n==1:
    return ['*']  #n이 1이면 *출력

  Stars=draw_stars(n//3)
  L=[]

  for star in Stars:
    L.append(star*3) # ***
  for star in Stars:
    L.append(star+' '*(n//3)+star) #* *
  for star in Stars:
    L.append(star*3) #***

  return L

N=int(input())
print('\n'.join(draw_stars(N)))
 



#4. 하노이탑 이동순서

def hanoi_tower(n, start, end) : #재귀함수
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계  #6-start-end하면 번호모를 막대 번호 알수 있음
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)


