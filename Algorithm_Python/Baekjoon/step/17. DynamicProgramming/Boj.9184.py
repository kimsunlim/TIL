#백준 9184 신나는 함수실행
#동적계획법

'''
재귀함수가 있다
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

##재귀호출 
#재귀함수 수행시간이 짧아지도록 구현

#재귀함수가 수행시간이 오래걸리는 이유는 매번 값을 계산하기 때문이다!
#그래서 DP로 한번 계산된 값은 저장하자!!

#값을 기록하기위한 3차선 그래프 
dp = [[[0 for _ in range(21)]for _ in range(21)]for _ in range(21)]

def w(a,b,c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b >20 or c > 20:
        return w(20,20,20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = (w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c))
        return dp[a][b][c]
    else:
        dp[a][b][c] = (w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1))
        return dp[a][b][c]

while True:
    a,b,c = map(int,(input().split()))
    if a == -1 and b == -1 and c== -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

