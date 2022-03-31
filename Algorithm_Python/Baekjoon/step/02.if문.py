#IF문

#Q1. BAEKJOON 1330_두수비교하기
#조건에 대한 Boolean값에 따라 출력값이 달라진다.

#1.두 수를 입력받는 코드를 작성
A,B = map(int,input().split())  #split()를 해야 공백을 기준으로 문자를 나눔!

if A>B:
    print('>') #if조건식이 참일때
elif A<B:
    print('<') #if조건식이 참이 아닌경우 elif조건식이 참일때
else:
    print('==')




#Q2.BAEKJOON 9498_시험성적
score = int(input())   #정수형식으로 입력받는 수 지정!!

if score>=90:
    print('A')

elif score>=80:
    print('B')

elif score>=70:
    print('C')

elif score>=60:
    print('D')

else:
    print('F')






#Q3.BAEKJOON 2753_윤년
# 연도가 주어졌을때, 윤년이면 1 아니면 0
# 윤년은 연도가 4의배수이면서,100의 배수가 아닐떄 또는 400의 배수일때다.


year =int(input())

if((year % 4 == 0) and (year% 100!= 0 or year % 400 == 0)):
    print('1')
else:
    print('0')



#Q4.BAEKJOON 14681_사분면고르기
#쫄지말고 사분면의 속성을 살펴보면된다.

X =int(input())
Y =int(input())

if X >0 and Y>0 :  #x,y가 모두 0보다 큰 1사분면!
    print(1)

elif X<0 and Y>0:  #x는 음수 y는 양수인 2사분면
    print(2)

elif X<0 and Y<0: #x는 양수 y는 음수인 3사분면
    print(3)

else:
    print(4)



#Q5.BAEKJOON 2884_알람시계

H,M =map (int, input().split())

if M < 45:  #분 단위가 45붐보다 작을때
    if H == 0: #0시이면
        H = 23
        M += 60
    else:   #0시가 아니면(0시보다 크면)
        H -= 1
        M += 60
print(H,M-45)
