# https://school.programmers.co.kr/learn/courses/30/lessons/120892

#암호해독

def solution(cipher, code):
    answer=''

    for i in range(code, len(cipher+1)):
        if i % code ==0:
            answer+=cipher[i-1]

    return answer 