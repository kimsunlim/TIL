
# Q1. 거스릅돈 문제
#당신은 점원이다. 거스름돈으로 사용할 500원, 100원,50원,10원 짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 주어야할돈이 n원일때, 거슬러 주어야 할 동전의 **최소 개수**를 구하라. 단, 거슬러 줘야 할 돈 n은 항상 10의 배수입니다.


n=1250
count=0

array=[500,100,50,10]

for coin in array:
    count+= n//coin
    n%=coin

print(count)


# Q2. 1이 될때까지
# 어떠한 수 N 이 1이 될때 까지 다음의 두과정중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할수 있다.

# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.

import split
n, k = map(int, input.split( ))

result=0

while True:
    target = (n//k)*k

    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k


result += (n - 1)
print(result)








#Q3. 곱하기 혹은 더하기


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 0혹은 1인경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

    print(result)



#Q4. 모험가 길드


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹수
count = 0  # 현재 그룹에 포함된 모험가의수

for i in data:  # 공포도를 낮은것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수 초기화
        result += 1  # 총그룹의 수 증가시키기
        count = 0  # 현재그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력


