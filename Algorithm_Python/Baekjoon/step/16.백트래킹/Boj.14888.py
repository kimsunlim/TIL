
#백준 14888 연산자 끼워넣기

# n개의 수와 n-1개의 연산자가 주어졌을때 , 만들수 있는 
#식의 결과가!! 최대 최소인 것

#DFS&백트래킹
#연산자는 앞에서 부터 차례대로 더하기, 빼기 .곱하기,나누기 연산자 실행

#첫번째 숫자에 첫 연산자를 넣고 DFS로 돌리고
#다시 백트래킹을 통해 원래 상태로 돌린후
#두번쨰 연산자를 넣고 DFS를 돌린 다음 다시 백트래킹으로 원래 상태를 돌려
#모든 경우의 수를 찾는다!!!
#그리고 이경우의 최대,최소 값을 다 찾는다



n=int(input()) #수의 개수
number =list(map(int,input().split())) #수열 입력
op=list(map(int,input().split())) #연산자 개수

#최댓값과 최솟값 초기화
minR =int(1e9) #1e9는 무한대 값 표현
maxR =-int(1e9)


answer=number[0]



def dfs(idx):
    global answer
    global minR, maxR
    
    if idx == n:
        if answer >maxR:
            maxR = answer
        if answer <minR:
            minR=answer 
        return
    
    for i in range(4):
        tmp=answer
        if op[i]>0:
            if i == 0:
                answer +=number[idx]
            elif i ==1:
                answer -= number[idx]
            elif i ==2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else: 
                    answer =(-answer // number[idx]) *-1
                    
            op[i]-=1
            dfs(idx+1)
            answer=tmp
            op[i] +=1
            
            
dfs(1)
print(maxR)
print(minR)



#코드참조: https://hongcoding.tistory.com/119





#전역변수란? global
#스크립트 전체에서 모든 요소에 접근가능
#함수 안에서 전역변수의 값을 변경하려면 global함수 선언













        