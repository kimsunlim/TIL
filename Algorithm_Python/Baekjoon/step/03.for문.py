
#01. 구구단
#N을 입력 받은뒤, 구구단 N단을 출력하는 츠로그램을 작성하시오

N=int(input())

for i in range(1,10): # 범위 9까지 for구문 돌아야한다!!
    print(N,'*',i,'=',N*i)



#02. A+B-3
#두 정수 a,b를 받은 다움 A+B출력하시오.

t =int(input()) #테스트 케이스 개수t개 받음

for _ in range(t): #t를 입력받아 범위로 돌것이다.
    a,b=map(int,input().split()) #공백으로 구분 문자열을 분리하여 정수로 변환
    print(a+b)



#03. 합
#n이 주어졌을때, 1부터 n까지 합을 구하시오

n= int(input())
sum = 0 # 합을 담을값 생성

for i in range(n+1): #n보다 1더 큰 수를 n과 더할것
    sum=sum +i
print(sum)


#04. 빠른 A+B
#Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

import sys
n=int(input())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)


#05. N찍기
#자연수 N이 주어졌을때 1부터 N까지 한줄에 하나씩 출력하시오

n=int(input())

for i in range(1,n+1):  #range(시작값, 종료값)
    print(i)



#06. 기찍 N
#자연수 N이 주어졌을때, N부터 1까지 한줄에 하나씩 출력하시오

n= int(input())

for i in range (n,0,-1):  # 초기값, 종료값 (해당값을 포함하지 않아서), 증가값을 넣어주는데 -1만큼 감소
    print(i)

    
    
    
    
    
    
 #7. A+B-7
# 두 정수 A와 B를 입력 받은 다음, A+B를 출력하시오

t= int(input())

for i in range(1, t+1): #1부터 t까지
    a, b=map(int, input().split())
    print(f'Case # {i}: {a+b}')







#8.A+B-8
# 두 정수 A와 B를 입력 받은 다음, A+B를 출력하시오


t = int(input())

for x in range(1, t+1):  # 1부터 t까지
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a+b}')






#9. 별찍기 -1
# 첫째 줄에는 별 1개, 둘째 줄에는 별2개, N번째줄에는 별 N개를 찍는 문제

n= int(input())

for i in range (1, n+1):
    print("*"*i)






#10. 별찍기 -2

n= int(input())

for i in range (1, n+1):
    print(" "*(n-i)+"*"*i) #공백이 n-i만큼 떨어져있다!! 조금만 더 깊게 생각 하면 보이는 특징!







#11.  x보다 작은 수
#정수 n개로 이루어진 수열 a와 정수 x가 주어진다. 이때, a에서 x 보다 작은 수를 출력하라
#반복이 아니라 값을 입력해야할때는 map함수를 써줘야한다!!

N,X = map(int, input().split())
A = list(map(int,input().split()))


for i in range(N):
    if A[i] <X:
        print(A[i],end=" ")

