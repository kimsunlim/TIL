# 백준 3036 링
#첫번째 링을 한 바퀴 돌렸을때 나머지 링이 몇바퀴 도는지 구하는 문제

#첫번째 숫자로 각 숫자의 최대공약수 구하기


import sys
input =sys.stdin.readline

N=int(input())
ring=list(map(int,input().split()))


#두수의 최대 공약수 구하는 함수(유클리드 호제법)

def findGCD (a,b):
    num = b
    div = a
    rest = b % a
    while rest !=0:
        num = div
        div = rest
        rest = num % div
    
    return div

# i번째 링도는 횟수 = 첫번째 링 반지름 / i번째 링 반지름

d= ring[0]

for idx in range(1,N):
    d_idx=ring[idx]
    GCD= findGCD(d, d_idx)
    print(f'{d//GCD}/{d_idx//GCD}')
    
    
#기약 분수를 만드는법 : 분자와 분모의 최대공약수를 분자, 분모에 각각 나눠준다
# i번째 링은 첫번째 링의 원주 만큼 회전하므로, 회전 바퀴수는 첫번쨰 링의 원주를 i번째
# 링의 원주로 나눠준 값이면 된다.
#유클리드 호제법으로 분자와 분모의 GCD를 구하고 분바 분모에 나눠준다.