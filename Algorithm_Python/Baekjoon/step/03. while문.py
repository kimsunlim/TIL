#10952번 A+B-5



while True:     #참이라면
    a,b =map(int,input().split()) #a,b를 입력받는다.
    if a == 0 and b ==0:   #a,b가 0이라면
        break;             #실행 종료
    else:                  #아니면 더하기
        print(a+b)




#10951번 A+B-4
#여러개의 테스트 케이스로 이루어져있다.
#입력 개수 제한이 없다>try,except로 하면 입력 되지않은 경우 종료된다.



while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break




#1110번 더하기 사이클

input = temp =int(input()) #사용자에게 숫자를 입력 받는고나서 int형으로 변형

cnt=0

while True:
    num1= temp //10  #십의 자리 수
    num2 = temp%10  #일의 자리 수
    sum_num =num1+num2 #십의 자리수와 일의 자리수 더한다.

    cnt +=1 #이 과정을 반복할떄마다 1번씩 카운팅하다가
    if input == temp : #같아지는 시점에 종료한다.
        break

print(cnt)



####################for 문과 while문의 차이

##############for문
#반복 횟수가 정해진 경우. 주로 배열과 함께 사용된다.
#for 변수 in 배열

for i in [1,2,3,4,5]: #배열이 온다.
    print(i)


for i in range(5): #5까지의 범위
    print(i)


#######3#while문
#무한루프나 특정 조건에 만족할때까지 반복해야하는경우
#주로 파일을 읽고 쓰기에 많이 사용한다.

i=0

while i<100: #조건
    print(i)
    i =i+1 #증감식


#break
i=1
while True:
    print('1')
    i+=1  #i 값을 1씩 증가하다가
    if i>3:     #3보다 크면 탈출
        break



#continue
i=1
while i<100:
    if i == 50 :
        print('continue')
        i+=1
        continue





