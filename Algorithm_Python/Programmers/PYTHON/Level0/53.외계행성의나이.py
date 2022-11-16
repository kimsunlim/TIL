#https://school.programmers.co.kr/learn/courses/30/lessons/120834
#외계행성나이

def solution (age):
    anwer=''
    apb=['a','b','c','d','e','f','g','h','i','j',]
    for i in str(age):
        anwer+= apb[int(i)]
    return anwer 
