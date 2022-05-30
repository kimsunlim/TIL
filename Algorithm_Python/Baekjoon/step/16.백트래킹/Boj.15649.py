# 백준 15649 N과 M(1)
#n까지 자연수 중 중복없이 m개를 고른 수열 >순열
#숫자를 선택하는 경우의 수로 이루어진 트리

#백트래킹
#브루트포스 전략을 취하지만, 처리 속도 향상을 위해 가지치기함



n,m = map(int,input().split())


s=[]

def f(): 
    if len(s) == m:       # 선택의 경우가 m이되면 해답
        print(' '.join(map(str,s)))
        return
    
    
    for i in range(1, n+1):  #숫자를 1부터 n까지 자연수중 선택
        if i in s:      #가지치기
            continue
        s.append(i)  #해당 경우의 수를 스택에 추가하고
        f()         #동작이 끝난후
        s.pop()     #다시 스택에서 빼내는 작업 필요
        
f()
