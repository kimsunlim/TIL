


# 프로그래머스 LV.1 콜라츠 추측


def solution(num):
    cnt=0
    while True:
        if num == 1:
            break
        if cnt == 500:
            break 
        if num%2 ==0:
            num=num/2
            cnt+=1
        else:
            num=num*3+1
            cnt+=1
    return cnt if cnt!= 500 else -1

#차분히 조건들은 하나씩 풀어나가면 된다
