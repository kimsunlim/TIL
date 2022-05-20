
#백준 1004 어린왕자
#도형이 배치된 모습을 잘 관찰하면서 아이디어 얻기

#출발점에서 도착점까지 이동할때, 중간중간에 위치한 행성들에 최소한으로 진입/이탈하는 문제

T = int(input())

for _ in range(T):
    # 출발점 도착점
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 행성계의 개수
    n = int(input())   #행성개수
    count = 0  #저장할 변수
    
    for _ in range(n):
        cx,cy,cr= map(int,input().split())   #각 행성의 좌표와 반지름
        dis1=(x1-cx)**2 +(y1-cy)**2
        dis2=(x2-cx)**2 +(y2-cy)**2
        pow_cr = cr**2
    
        if pow_cr > dis1 and pow_cr > dis2:
            pass
        elif pow_cr > dis1:
            count += 1
        elif pow_cr > dis2:
            count += 1
            
    print(count)

        

