# 백준 9375 패션왕 신해빈
# 경우의 수 연습문제

#(종류별 옷의 수) + 1을 전부 곱해주고 (해당 종류의 옷을 안 입는 경우의 수를 포함한 것)
#알몸의 경우의 수인 1만 빼주면 됨

T = int(input())

for _ in range(T):
    n = int(input())
    
    #0일때 탈출
    if n == 0:
        print(0)
        continue
    
    wearable =dict()
    for _ in range(n):
        wear_name, wear_type = map(str, input().split())
        
        #같은 옷 분류 중, 이름은 버리고 종류만 가져가기
        if wear_type in wearable.keys():
            wearable[wear_type] += 1
        else:
            wearable[wear_type] = 1
        
        #(각 옷의 수)+1 한 것을 곱해줌
        answer = 1
        for key in wearable.keys():
            answer *= wearable[key] + 1
    #안입는 경우만 뺴줌
    print(answer - 1)