def solution(my_string):
    return my_string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    
    ##이렇게 반복되는 것을 없앨땐 for문 쓰기 

    def solution(my_string):
        a= ['a','e','i','o','u']
        for i in a:
            my_string= my_string.replace(i,'')
        return my_string