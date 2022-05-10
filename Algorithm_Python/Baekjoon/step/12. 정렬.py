# -*- coding: utf-8 -*-


#정렬: 배열의 원소를 순서대로 나열하는 알고리즘



#백준 2750 수정렬하기
#시간 복잡도가 O(n²)인 정렬 알고리즘으로 풀 수 있음. 예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.
#sort함수로 정렬 쉽게 구현 

n= int(input())
num_list=[]  #이 안에 넣어줄것

for _ in range(n):
    num_list.append(int(input())) #리스트에 넣기

num_list.sort()

for i in num_list:
    print(i)
    #솔트 된걸 하나씩 출력!!
    
    
    
#백준 2751 수정렬하기2
#input을 쓸때 시간초과 >prompt message를 출력하고 개행을 삭제한값을 리턴해서 느림
#반복문으로 여러줄 입력받을땐, sys.stdin.readline() 사용하면 시간초과 안남


import sys
n= int(sys.stdin.readline())
num_list=[]  #이 안에 넣어줄것

for _ in range(n):
    num_list.append(int(sys.stdin.readline())) #리스트에 넣기

num_list.sort()

for i in num_list:
    print(i)
    #솔트 된걸 하나씩 출력!!
    
    
    
    
#백준 10989 수정렬하기3
#카운팅 정렬로 더 빠르게 정렬 가능

import sys
n=int(input(sys.stdin.readline()))

num_list=[0]*10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            
            print(i)
            
            
            
            
            
          
#백준 2108 통계학
#sys.stdin.readline()과 친해지기input과 확연한 속도 차이가난다!

import sys
from collections import Counter


n=int(sys.stdin.readline())     
li=[] #값을 넣을 리스트 생성


for _ in range(n):
    li.append(int(sys.stdin.readline()))
    
    #n까지 레인지 돈것을 리스트에 담는다.
    
#산술평균
print(round(sum(li)/n))   #여러수를 더해서 나눠야할때는 꼭 리스트 파일 이전에 생성할것!

#중앙값 :오름차순 >중간값
li.sort() #오름차순
print(li[n//2]) #중간의 값 인덱스로 찾기

#최빈값 :빈출

cnt_li =Counter(li).most_common()  #counter 안에있는 문자 갯수반환, 데이터 개수가 많은 순으로 정렬
if len(cnt_li)>1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개이상
    print(cnt_li[1][0])
    
else:
    print(cnt_li[0][0]) #최빈값이 하나일때
    


#범위   
print(max(li)-min(li))
    




#백준 1427 소트인사이드
#숫자를 정렬,내림차순으로
#오름 차순으로 넣었다가 정렬 내림차순으로 변경
# 그 후 다시 추출


n= int(input())

li=[]

for i in str(n):
    li.append(int(i))  #int형으로 넣어야하기에 int꼭 붙이기
    
li.sort(reverse=True)#내림차순

for i in li:
    print(i,end='') #내림차순 추출
            
            
            
            
#백준 11650 좌표정렬하기        

import sys


n=int(sys.stdin.readline())   
            
li=[]

for i in range(n):
    x,y= map(int,input().split())
    li.append((x,y))    #출력하변[[3,4],[1,1],[1,-1]] 이런식으로추출
    
li.sort() #오름차순으로 정렬!

for i in range(n):
    print(li[i][0],li[i][1]) #리스트 안에 있는 리스트 추출
    
    


    
               
#백준 11651 좌표정렬하기2
            
            
import sys

n=int(sys.stdin.readline())   
            
li=[]  

for i in range(n):
    x,y= map(int,input().split())
    li.append([y,x])    #출력하변[[3,4],[1,1],[1,-1]] 이런식으로추출
    
li_s=sorted(li) #오름차순으로 정렬!

for y,x in li_s:
    print(x,y)#        
            
            
            
            
            
#백준 1181 단어정렬

n=int(input())
li=[]



for i in range(n):
    li.append(input())
    #n변수로 단어 개수를 입력받고 li리스트에 단어를 추가한다
    
set_li =list(set(li))#set으로 중복을 제거 또한 자료형으로 바껴서 리스트로 변환해줄것


sort_li=[]

for i in set_li:  #중복제거한 단어리스트를 돌린다
    sort_li.append((len(i),i)) #단어길이와 단어로 묶어서 저장한다! 중요!
    
result= sorted(sort_li)  #sorted 쓰면 앞에있는 숫자와 뒤에있는 문자가 정렬!

for len_li, li in result:
    print(li)

    
    
      

            
#백준 10814 나이순정렬    
#람다활용!       
            
            
n=int(input())
ls=[]




for _ in range(n):
    age,name=map(str,input().split())
    age=int(age) #문자형을 숫자형으로 변환!
    ls.append((age,name))
  
    
ls.sort(key= lambda parameter_list: parameter_list[0])
#(파라미터: 리턴 값)

"""
람다는 이름없는 함수
위의 코드는

def ladmbda(parameter_list):
    return parameter_list[0]
인덱스 0에 해당하면age, 1에 해당하면 name으로 정렬함


"""


for i in ls:
    print(i[0],i[1])





#백준 18870 좌표압축

import sys
input = sys.stdin.readline

n = int(input())
dic = {}

nums = list(map(int, input().split()))
sNums = sorted(set(nums))

for i in range(len(sNums)):
    dic[sNums[i]] = i

for j in nums:
    print(dic[j], end=' ')
    












            
            
            
            