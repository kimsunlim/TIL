from collections import Counter 

def solution(array):
    a= Counter(array).most_common(2)  
    
    #most_common메소드는 등장한 횟수를 내림차순으로 정리해서 보여줌

    if len(a)==1:
        return a[0][0]
    if a[0][1]==a[1][1]:
        return -1
    return a[0][0]  #첫번째 요소에서 첫번째 값만 추출!!