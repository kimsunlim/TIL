#https://school.programmers.co.kr/learn/courses/30/lessons/120844
#배열회전시키기
#deque는 양방형 자료형으로 앞뒤에서 데이터를 처리

from collections import deque

def solution(numbers,direction):
    num_deque =deque(numbers) #리스트를 deque형식으로
    if direction =='right':
        num_deque.rotate(1) #오른쪽
    else:
        num_deque.rotate(-1) #왼쪽
    return list(num_deque)


