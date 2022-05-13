# -*- coding: utf-8 -*-

##집합과 맵
#특정원소가 속해있는지 빠르게 찾거나, 대응되는 원소를 빠르게 찾는 구조!


#10815 숫자카드
#내가 입력한 숫자들이 상근이가 가지고 있는지 확인
#이진탐색 Binary Search
# 데이터가 정렬돼 있는 배열에서 특정한 값 찾는 알고리즘!
# 배열의 중간에 있는 값을 선택하여 찾고자하는 x와 비교한다
#x가 중간 값보다 작으면 좌측 크면 우측을 대상으로 다시 탐색한다

import sys


n= int(input()) #상근이 숫자 카드 개수
card=list(map(int,sys.stdin.readline().split())) #상근이 숫자카드 목록
m=int(input()) # 내 카드 개수
check=list(map(int,sys.stdin.readline().split())) #내 숫자카드 목록

card.sort()

##기본적인 이분탐색 코드
def binary_search(array, target, start, end):
    while start <= end:   #start가 end보다 작다는것 지정
        mid=(start+end)//2  #중간값 지정
        
        if array[mid] == target:
            return mid
        elif array[mid] >target:
            end= mid-1
        else:
            start =mid +1
    return None
    
    
#상근이가 가지고 있으면 1출력 아니면 0출력    
for i in range(m):
    if binary_search(card, check[i], 0, n-1) is not None:
        print(1, end='')
        
    else:
        print(0, end='')
        
        
        
        










#14425 문자열집합

import sys


n, m = map(int, sys.stdin.readline().split())
s = [str(sys.stdin.readline()) for _ in range(n)] # n을 포함한 집합 s
cnt = 0

# 반복문을 통해 m개의 문자열을 확인
for i in range(m):
    word = str(sys.stdin.readline())

    # 집합 s에 문자열이 포함되어 있으면 카운트
    if word in s:
        cnt += 1

print(cnt)










#1620 포켓몬마스터



import sys

N, M = map(int, input().split())
number_pokemon = 1
pokemon_dict1 = {}
pokemon_dict2 = {}

for _ in range(N):
    name = str(sys.stdin.readline()).strip()
    pokemon_dict1[number_pokemon] = name
    pokemon_dict2[name] = number_pokemon
    number_pokemon += 1

answer = []
for _ in range(M):
    pokemon = str(sys.stdin.readline()).strip()
    try:
        print(pokemon_dict1[int(pokemon)])
    except:
        print(pokemon_dict2[pokemon])
    







#10816 숫자카드2

#  찾고자하는 숫자와, 개수까지 구해야함
# 사전 이용풀이




n= int(input())
cards = list(map(int,input().split(' ')))
cards.sort()

m=int(input())
targets=list(map(int,input().split(' ')))
dic=dict()

for i in cards:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end='')
        
    else:
        print(0, end='')
        




#1269 대칭차집합
#set을 이용하면 차집합 구할수 있음
#집합에 공통요소가 없기때문에 set으로 입력받기

n,m = map(int,input().split())

a=set(map(int,input().split()))
b= set(map(int,input().split()))

print(len(a-b)+len(b-a))





#1764 듣보잡

n,m = map(int,input().split())
li1=set()
li2=set() #중복제거


for _ in range(n):
    li1.add(input())
    
for _ in range(m):
    li2.add(input())
    
li= sorted(list(li1 & li2)) #교차하는 이름 찾
print(len(li))

for i in li:
    print(i)






#11478 서로다른부분 문자열의 개수

s=str(input())

li=[]

for i in range(len(s)): #i부터 s전체 길이까지
    for j in range(len(s)-i):
        li.append(s[j:j+i+1])
        
print(len(set(li)))



#이중반복문 쓰는거 익숙해지기!!!
















