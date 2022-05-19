#백준4153 직각 삼각형


#피타고라스 법칙
#직각 삼각형이라면 a**2+b**2=c**2 이 성립한다


while True:
    nums=list(map(int,input().split()))
    if sum(nums)==0:
        break
    #세 수합이 0이라면 빠져나오기
    
    max_num =max(nums) #가장 큰 빗변찾기
    nums.remove(max_num) #그리고 삭제, 젤 큰걸 리스트 안에서 따로 지정할수가 없다.
    
    if nums[0]**2 + nums[1]**2 ==max_num**2:
        print('right')
        
    else:
        print('wrong')
