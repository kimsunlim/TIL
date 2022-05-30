# 백준 15650 N과 M(2)

#백트래킹

#중복 노노
#오름차순 정렬


n,m = map(int,input().split())


s=[]

def f(start): 
    if len(s) == m:       # 선택의 경우가 m이되면 해답
        print(' '.join(map(str,s)))
        return
    
    
    for i in range(start, n+1):  #숫자를 start지점부터 n까지 자연수중 선택
        if i in s:      #가지치기
            continue
        s.append(i)  
        f(i+1)         
        s.pop()    
        
f(1)

#start 변수추가 기존에는 1부터 시작했지만 이번경우는 앞의 숫자가 더 클수도 있기에
#변수 설정
