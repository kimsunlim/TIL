# 프로그래머스 LV.1  최대공약수와 최소공배수


#유클리드 호제법
#최대공약수 구하는 알고리즘
#서로 상대방수를 나누어 원하는 수를 얻는 방식
#a,b를 나눈 나머지가 r이면 a와 b의 최대공약수는 b과 r의 최대공약수와 같다


def gcd(n,m):
    mod = m % n  #mod 나머지
    if mod != 0: #mod 가 0이 아니라면
        m, n = n, mod  #m,n과 n,mod 가 같은게 유클리드 호제
        return gcd(n, m)  #최대공약수 리턴
    else:
        return n

def solution(n,m):
    return [gcd(n,m),int(m*n/gcd(n,m))]