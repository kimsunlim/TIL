# 백준 11051 이항계수2

#더 넓은 범위의 이항계수를 동적 계획법으로 구하는 문제

from math import factorial

n,k = map(int,input().split())

b= factorial(n)//(factorial(k)*factorial(n-k))

print(b % 10007)


# / 나누기
# // 몫
# % 나눈 나머지