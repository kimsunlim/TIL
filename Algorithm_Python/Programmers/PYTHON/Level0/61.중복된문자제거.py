#https://school.programmers.co.kr/learn/courses/30/lessons/120888
#중복된 문자제거
def solution (my_string):
    answer=''
    for i in my_string:
        if not i in answer:
            answer+=i 
    return answer
