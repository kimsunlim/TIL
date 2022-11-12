#대문자와 소문자
#https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer=''
    for i in my_string:
        if i.islower():
            answer+=i.upper()
        elif i.isupper():
            answer+=i.lower()