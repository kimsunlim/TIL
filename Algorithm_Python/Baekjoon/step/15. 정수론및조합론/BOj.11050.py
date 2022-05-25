# 백준 11050 이항계수 1

#n개의 물건 중 순서를 고려하지않고 k개를 고르는 경우 

from math import factorial

n,k =map(int,input().split())

print(factorial(n) // (factorial(k)* factorial(n-k)))


#  nCk 즉, n! / k!(n - k)!