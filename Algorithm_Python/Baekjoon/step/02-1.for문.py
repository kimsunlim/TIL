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



