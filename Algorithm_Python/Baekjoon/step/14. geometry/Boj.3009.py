#백준 3009 네번째 점
#리스트로 찾기

#x좌표로 이루어진 네개의 수
#y좌표로 이루어진 네개의 수




x_nums=[]
y_nums=[]

for _ in range(3):  #3번 입력받아 반복
    x,y= map(int,input().split())
    x_nums.append(x)
    y_nums.append(y)
    
    
for i in range(3):
    if x_nums.count(x_nums[i]) ==1:  #리스트에서 개수가 한개인 요소 찾기
        x4 = x_nums[i]
        
    if y_nums.count(y_nums[i]) ==1:
        y4 =y_nums[i]
        
print(x4,y4)
    
