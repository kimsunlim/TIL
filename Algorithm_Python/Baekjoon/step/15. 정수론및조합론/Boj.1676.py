#백준 1676 팩토리얼 0의개수

# 소인수분해의 성질을 활용하여 N!의 끝에 0이 얼마나 많이 오는지 구하는문제

#5! =120
#10!=3628800  >>뒤의 0의개수


n= int(input())

cnt=0
while n>0:
   cnt+=n//5
   n//5
    
print(cnt)


