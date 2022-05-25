#백준 2981 검문
#n개의 수를 m으로 나누었을때, 나머지가 전부 같은 m을 찾는 문제

# n 주어진 숫자 ,m 나눠지는 숫자, r나머지


    

import math
t = int(input())
s = []
a = []
gcd = 0
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)
a.append(gcd)
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')