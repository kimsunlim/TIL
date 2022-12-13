# 팩토리얼


import math 
def solution(n):
    k=10
    while n < math.factorial(k):
        k-=1
    return k