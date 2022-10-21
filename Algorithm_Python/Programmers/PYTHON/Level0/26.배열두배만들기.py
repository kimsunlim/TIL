def solution(numbers):
    answer=[]

    for i in numbers:
        answer.append(i*2)
    return answer



######
def solution (numbers):
    return[numbers[i]*2 for i in range(len(numbers))]