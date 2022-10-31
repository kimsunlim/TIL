def solution (num,k):
    num=str(num)
    k=str(k)
    if num.find(k)==-1:
        return -1
    else:
        return num.find(k)+1


    ##find 인텍스 추출 함수, 없는 경우엔 -1을 추출함