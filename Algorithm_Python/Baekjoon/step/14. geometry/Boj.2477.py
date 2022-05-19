##백준 2477 참외밭
#특정한 형태의 도형의 넓이를 구하는 문제




#point
#참외밭은 ㄱ자 모양, 혹은 이를 회전한 ┏, ┗, ┛ 모양의 육각형이다.
#참외밭의 둘레를 돌면서 지나는 변의 방향은 반시계방향으로 주어진다.
#변의 방향은 동,서,남,북 순서로 1,2,3,4의 값을 가진다.
#출발 꼭지점은 "임의"로 주어진다




#tip
#육각형을 직사각형의 모양으로 확장한 뒤, 비어 있는 부분을 분리
#최종 답 = ( 1m^2 당 참외 개수 K ) * ( 큰 박스 넓이 - 작은 박스 넓이 ) 




melon = int(input()) # 참외 개수 K
values = [input().split() for _ in range(6)] # 나머지 2~7 line의 6 줄을 입력 받는다.
directions = [int(v[0]) for v in values] # 방향을 뽑아내서 저장한다.
lengths = [int(v[1]) for v in values] # 길이를 뽑아내서 저장한다.
max_lengths, box_lengths = [], [] # 큰 박스의 길이, 작은 박스의 길이를 담을 배열

for i in range(1, 5):
    if directions.count(i) == 1: # direction이 한번만 존재한다 == 큰 박스의 변
        max_lengths.append(lengths[directions.index(i)]) # 큰박스의 변 길이 저장
        temp = directions.index(i) + 3 # 큰 박스 + 3 == 작은 박스의 변
        if temp >= 6:
            temp -= 6 # cycle을 위해 6 이상일 경우 -6
        box_lengths.append(lengths[temp]) 

area = max_lengths[0] * max_lengths[1] - box_lengths[0] * box_lengths[1]
print(melon * area)
