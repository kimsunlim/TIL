
# 백준15651 N과 M(3)
# 백트래킹

# 중복허용

n,m=map(int,input().split())

s=[]

def f():
    if len(s) ==m:
        print(' '.join(map(str,s)))
        return
        
        
    for i in range(1,n+1):
        s.append(i)
        f()
        s.pop()
        
        
f()


