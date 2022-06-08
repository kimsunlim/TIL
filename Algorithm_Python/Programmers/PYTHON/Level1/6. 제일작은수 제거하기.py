# 프로그래머스 LV.1  제일 작은 수 제거하기






def solution(arr):
    arr.remove(min(arr))  #배열의 최솟값 제거
    if len(arr) ==0:      #배열이 없는 0인거 -1로 리턴 ( 숫자 하나만 있을떄 배열 0)
        return[-1]
    return arr
    
