# 프로그래머스 LV.1 행렬의 덧셈

# 정, 문자의 덧셈이 아니라
#행렬의 덧셈이다!!!
#행렬덧셈 주의하고 연습!!


# 숫자를 받고 행과 열끼리 더해준다



def solution(a,b):
    for i in range(len(a)): #a의 행렬 길이까지 다 돈다음
        for j in range (len(a[i])): #행렬 a의 안에 첫번째 인자도 돌아준다
            a[i][j] += b[i][j] #a에 b행렬을 더해준다 ##w지정해줘야
            
    return a
