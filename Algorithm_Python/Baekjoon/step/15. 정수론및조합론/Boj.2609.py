
#백준 2609 최대공약수와 최소 공배수

#유클리드 호제법
#두 수가 서로 상대방 수를 나누어 결국 원하는 수를 앋는 알고리즘


a,b=map(int,input().split())

def gcd(a,b):  #최대공약수
    while b>0:
        a,b = b, a % b
    return a
    
def lcm(a,b):   #최소공배수= a,b곱을 a,b최대 공약수로 나누면됨
    return a * b // gcd(a,b)



print(gcd(a,b))
print(lcm(a,b))

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))