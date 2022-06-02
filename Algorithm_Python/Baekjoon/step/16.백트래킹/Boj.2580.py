
#백준 2580 스도쿠

#DFS+백트래킹

#문제에서 빈칸은 0이 주어지므로 graph의 0칸의 위치 정보를 blank리스트에 넣어준다
#첫번째 빈칸에 1~9까지의 수중 넣을 수 있는 수를 넣는다
#그 다음 빈칸에대해서도 같은 방법 수행

import sys 
graph=[]
blank=[]

for i in range(9):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            blank.append((i,j))
            
def checkRow(x,a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y,a):
    for i in range(9):
        if a ==graph[i][y]:
            return False 
    return True


def checkRect(x,y,a):
    nx =x //3*3 
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+i]:
                return False
            
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
        
    for i in range(1,10):
        x= blank[idx][0]
        y= blank[idx][1]
        
        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            graph[x][y] =i 
            dfs(idx+1)
            graph[x][y]=0
            
dfs(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        