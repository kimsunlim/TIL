
def solution(numbers):  #numbers라는 정수배열
    numbers.sort(reverse =True) #큰 순서대로 배열을 정렬
    return numbers[0]*numbers[1]