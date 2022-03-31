# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:53:01 2022

@author: KMMD011
"""

##문자열
#Q1. 아스키코드

n=input()

print(ord(n))

#ord문자의 아스키코드값 리턴
#chr 아스키모드값받아서 그 코드에 해당하는 문자 출력




#Q2. 숫자의합
a=int(input())
n=list(input())

sum=0
for i in n:
    sum+=int(i)
 
print(sum)




#Q3.알파벳 찾기

s= input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in s:
        print(s.index(i),end='')   # 위치출력은 인덱스로 s.index(i)
        
    else:
         print(-1, end='')
         
         


#Q4.문자열반복

t=int(input())



for i in range(t):
    r,s=list(map(str,input().split()))
    r= int(r)
    
    for i in s:
        print(r*i,end='')
    print()
    
    
    
    
   
#Q5.단어공부
##대문자와소문자를 구분하지않는다>첫째줄에 대문자로 출력

#upper로 대문자로 변환
#set함수써서 중복 문자값 제거
#for 써서 횟수 저장
#if로 출력문저장한다음에 1보다크면 ?출력


word = input().upper( ) #대문자 변환
word_list=list(set(word)) #중복제거

cnt=[]

for i in word_list:
    count= word.count #단어 카운트/count는 문자열 메서드
    cnt.append(count(i))
    
if cnt.count(max(cnt))>1:  #맥스 값이 1보다 크면 ?출력
    print("?")
    
    
else:
    print(word_list[(cnt.index(max(cnt)))]) #가장큰 맥스의 위치 index로 찾음
    






#Q6.단어의개수


word=input().split()

print(len(word)) #len문자열 메소드, 매개변수로 들어온 문자열 길이 반환

    
    


#Q7. 상수

A,B= input().split()

A= int(A[::-1])  #숫자 거꾸로 읽게 변환  [시작인덱스:종료인덱스:step]
B=int(B[::-1])

if A>B:
    print(A)

else:
    print(B)
    



#출력 플러스
print(max(A,B))

                          



#Q8.다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a= input()

#걸리는 시간
ret=0

for i in range(len(a)):
    for j in dial:
        if a[i] in i:   #입력 받은 a가 i의 문자열에 해당한다면 +3초
            ret+= dial.index(i)+3
            
print(ret)



#Q9.크로아티아 알파벳
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b= input()

for i in a:
    b= b.replace(i,"a")   #b에 a안에 있는 문자로 바꿈
print(len(b))

    

#Q10. 그룹단어체커
N = int(input())   #단어개수 입력
cnt = N

for i in range(N):
    word = input()   #단어입력
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]: #두번째 이사으이 단어부터 j와 같지 않으면 -1해주기
            cnt -= 1
            break

print(cnt)       
            




