

#백준 1002 터렛
#두 원의 교점의 개수를 구하기

#두 원의 중심과 반지름을 입력했을때, 두 원사이의 접점의 개수구하는 문제!


import math

T = int(input())

for _ in range(T): #테스트케이스 돌면서
    x1,y1,r1,x2,y2,r2 =list(map(int, input().split()))
    
    #두 원의 중심 사이의 거리/터렛 좌표사이거리
    dis= math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    ##접점 출력
    
    if dis ==0: # 두 원의 중심이 같을 경우
        if r1 == r2: #두 원의 크기가 같아 겹치는 경우
            print(-1)
            
        else:        #한원이 다른 원 안에 들어가 있는경우
            print(0)
            
    else:      #두 원의 중심이 다른경우
        if r1+r2 == dis or abs(r2-r1) ==dis: #한점에서 만나는경우
            print(1)
            
        elif ((abs(r1-r2) < dis ) and (dis<r1+r2)):  #두점에서 만나는경우
            print(2)
            
        else:
            print(0)
    
    
    
    

