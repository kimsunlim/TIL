def solution (n,num_list):
    answer=[]
    for i in numlist:
        if i%n==0:
            answer.append(i)
    return answer