# 내풀이 
def solution(n,k):
    if n<10:
        answer=(n*12000)+(k*2000)
    elif n>=10:
        answer=(n*12000)+(k*2000)-(n//10*2000)
    return answer 

## 코드가 불필요하게 길다. 간단하게 합쳐보자

def solution (n,k):
    service=n//10
    answer=(n*12000)+(2000(k-service))
    return answer