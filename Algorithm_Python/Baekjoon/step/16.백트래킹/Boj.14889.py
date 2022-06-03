
#백준 14889 스타트와 링크
# 두팀으로 나누어서 능력치 차이를 최소로 하게 팀을 구성


#1. 팀을 구성하는 함수
#2. 팀의 능력치 차이를 계산하는 함수



#팀 능력치 차이 계산

def cal_diff(team1, team2):
    sum_team1=0
    sum_team2=0
    
    for i in range(len(team1)):
        for j in range(len(team1)):
            
            sum_team1 += arr[team1[i]][team1[j]]  # Sij
            sum_team2 += arr[team2[i]][team2[j]]
            
            
        return abs(sum_team1 - sum_team2)
    
    
#팀구성 함수

def make_team (team1, count, N, start):
    global answer
    
    if count == N//2:  #2개의 팀으로 구성
        team2=[]
        
        for i in range(N):
            if i not in team1:
                team2.append(i)
                
        local_diff =cal_diff(team1, team2)
        answer =min(answer, local_diff)
        return
    
    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            make_team(team1, count+1, N,i+1)
            team1.remove(i)
            
            
if __name__=='__main__':
    N= int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]
    answer= int(1e9)
    make_team([],0,N,0)
    print(answer)
            
            
    