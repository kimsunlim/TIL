#1차원 array


#Q1.
#10818번 최소,최대
# 첫째줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
#map은 map객체를 반환하므로 list함수로 형변환 해주면 각 원소가 숫자인 내가 원하는 배열을 찾을수 있다.

input()  #인풋값을 넣고
arr= list(map(int,input().split())) #list로 형변환하여 원하는 배열 찾는다
print(min(arr), max(arr))





#Q2.
#2562번 최댓값
#최댓값을 찾고 그 최댓값이 몇번째 수인지 구해라
#입력값이 9개로 정해져있다!!
#배열을 하려면 리스트에 넣어 숫자들을 나눠줘야한다.

num_list=[]

for i in range(9):    #9번 반복하기위해 for구분에 범위 설정
    num_list.append(int(input()))  #1회 반복할때마나 list append한다

print(max(num_list))
print(num_list.index(max(num_list))+1)  #인덱스는 0부터시작하니 +1을 꼭해줘야한다.





#03.
#2577번 숫자의 개수
#0~9까지 숫자가 몇번 쓰였는지 구하기

a = int(input())
b = int(input())
c = int(input())
num= a *b*c
num_list=list(str(num)) #곱한값을 문자열로 반환하여 문자요소를 가지는 리스트로 변환한다

for i in range(10): #0~9 몇번 쓰였는지 포구문을 돌것
    num_list_count =num_list.count(str(i))  #카운트 함수로 그 리스트가 몇개씩 있는지 프린트해준다!!
    print(num_list_count)




#04.
#3052번 나머지



arr=[]
for i in range(10):
    n = int(input())
    arr.append(n%42)  #입력값을 append한 다음에 나눠줘야한다
arr=set(arr)  #set함수는 중복을 제거함
print(len(arr))   #나머지가 몇개있는지 출력




#05.
#1546번 평균

n=int(input())
score = list(map(float, input().split()))

max=0

for i in range(n):
    if max<score[i]:
        max=score[i]

for i in range(n):
    score[i]=(score[i]/max)*100

sum =0
for i in range(n):
    sum+=score[i]

print(sum/n)


#06.
#8958번 ox퀴즈
#ox점수를 구하는 프로그램을 만들어라 개어렵넹.. ㅎㅎㅎ
#1. O일때 연속하여 몇번 o가 들어왔는지 카운트하기
#2. O일떄, 임의의 변수에 카운트한 수 더하기
#3. X일때 카운트한 수를 0으로 초기화한다.


n= int(input())
for _ in range(n):
    count=0
    sum=0

    a =list(input()) #인풋함수 리스트로 변환시켜주는거 중요하다!!잊지말자 자꾸 까먹는다!!
    for i in a:
        if i =='o':
            count+=1
            sum =sum+count
        else:
            count=0
    print(sum)




#07.
#4344번 평균은 넘겠지
#1. 테스트 케이스 개수 C
#2. 학생수가 첫 수로 주어지고, 이어서 n명의 점수가 주어진다.
#3. 한줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째자리 까지 출력한다.

n= int(input())

for i in range(n):
    a= list(map(int,input().split()))
    avg =(sum(a)-a[0])/a[0]
    count = 0
    for j in a[1:]:
        if j >avg:
            count+=1

    print("%.3f%%" % ((count /a[0])*100))











###학습리뷰
#1. list로 변환하면 array 찾을수 있다!
#2. 코드 줄줄이 쓰는걸 귀찮아하면 안된다!!! 줄이는걸 먼저 고민하다가 틀린다ㅠ