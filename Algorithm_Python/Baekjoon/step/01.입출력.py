# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:26:08 2022

@author: KMMD011
"""

###입출력과 사칙연산
#백준 
#1 Hello World

print("Hello World")


#2.

print("강한친구 대한육군\n"*2)


#3. A+B

A,B= input().split()

print(int(A)+int(B))



#4. A-B

A,B= input().split()

print(int(A)-int(B))


#5. A*B

A,B= input().split()

print(int(A)*int(B))


#6. A/B

A,B= input().split()

print(int(A)/int(B))

#7. 사칙연산




a,b = input().split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b)) #int 없으면 float형으로 출력 그래서 int 붙여줘야함
#print(a//b)
print(a%b)

#8.??!


print(input() + "??!")
 
#어렵게 생각할 필요가 없다!
#아이디를 입력하는 것은 input함수를 통해서 한다.
#그래서 바로 input을 쓰고 기호식을 뒤에 붙여주면 된다!


#9.1998년생인 내가 태국에서는 2541년생?

#서기연도 사용 >>태국만 불기연도 사용
#불기연도를 서기 연도로 변환

#2541 >1998

a=int(input())

print(a-543)


#10. 나머지

A,B,C= map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')

##map 함수는 여러개의 데이터를 한번에 다른 형태로 변환하기 위해 사용함



#11. 곱셈

num1= int(input())
num2= int(input())

print(num1 * (num2%10))  #num2를 10으로 나눈 나머지
print(num1 * ((num2%100)//10)) #num2를 100으로 나눈 나머지에 10을 나눔
print(num1 * (num2//10)) #num2를 100으로 나눈 몫
print(num1*num2)













