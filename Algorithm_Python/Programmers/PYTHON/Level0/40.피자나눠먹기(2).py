def solution (n):
    pizza=6
    while pizza % n !=0:
        #같은 수로 나눠질때까지 +6
        pizza +=6
    return pizza /6 
    