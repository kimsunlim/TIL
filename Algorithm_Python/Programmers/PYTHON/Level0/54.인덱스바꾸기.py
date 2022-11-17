def solution(string,num1,num2):
    s=list(string)
    s[num1],s[num2] = s[num2]=s[num1]
    return ''.join(s)