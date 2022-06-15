
# 프로그래머스 LV.1 하샤드 수 


#1. x자릿수의 합
#2. x/x자릿수합
#3. x/x자릿수합이 하샤드인지 아닌지 판별



def solution(x):
    a=list(map(int,str(x)))
    s=sum(a) #x자릿수의 합
    
    if x%s==0:  #x/x자릿수합
        x=True   # x/x자릿수합이 하샤드인지 아닌지 판별
    else: 
        x=False
    return x