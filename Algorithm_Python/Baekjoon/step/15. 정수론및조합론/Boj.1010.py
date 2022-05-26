#백준 1010 다리놓기

# 다리를 놓는 경우의 수를 구하는 문제


#다리끼리 서로 겹쳐질 수 없다고 할때 다리를 지을수 있는 경우의수

##조합
#m이 n보다 크기때문에 최대 연결할수 있는 다리갯수 n개
#m개 지역에 n개 다리를 놓을수 있는경우
#m! 을 (m-n)!n! 으로 나눈 값



import math

t= int(input())

for _ in range(t) :

    n,m=map(int(),input().split())
    bridge = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
    print(bridge)
    
    