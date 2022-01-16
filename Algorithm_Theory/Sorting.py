##정렬알고리즘
##데이터를 특정한 기준에 따라 순서대로 나열 하는 것

##1. 선택 정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는것을 반복
# 0~7 의 카드가 섞여있다면 0을 맨앞으로 보내는 것

array =[7,5,9,0,3,1,6,2,4,8]  #리스트에 저장

for i in range (len(array)):
    min_index = i  #가장 작은 원소의 인덱스
    for j in range(i+1, len (array)):
        if array[min_index]>array[j]: #현재 작은 원소보다 더 작은 j원소가 있다면
            min_index = j             #minindex는 j 가 되고 결과적으로 안쪽 반복문을 돌았을떄 가장 작운 원소 추출
    array[i],array[min_index]=array[min_index],array[i]  #그래서 가장 작은 인덱스와i의 위치를 바꿔줌

print(array)




##2. 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 난이도가 있지만 더 효율적

array =[7,5,9,0,3,1,6,2,4,8]

for i in range (1, len(array)): #2번쨰 데이터 부터 마지막 데이터까지 포구문
    for j in range(i,0,-1):  #인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] <array[j -1]:  #한칸씩 왼칸으로 이동    #j의 값이 더 작을떄
            array[j],array[j -1] = array [j-1], array[j]   #값의 위치를 바꿔줌
        else: #자기보다 작은 데이터가 나오면 멈춤
            break



##3. 퀵정렬
# 기준 데이터를 정하고 그 기준보다 큰데이터와 작은데이터 위치를 서로 바꾸는 방법
# 기본적으로 첫번째 데이터를 기준 데이터 (pivot)로 설정
# 병합정렬과 더불어 가장 많이 사용!

#피벗을 기준으로 데이터 묶음을 나누는 작업을 '분할'이라고 함

array =[7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: #원소가 한개인 경우 종료
        return
    pivot =start
    left= start +1
    right= end

    while(left <= right):  #레프트 변수가 라잇 변수보다 작아질때까지 반복!

        # 피벗보다 큰 데이터를 찾을때까지 반복
        while( left <= end and array[left] <= array[pivot]):
            left +=1
        # 피벗보다 작은 데이터를 찾을때까지 반복
        while( right> start and array[right]>= array[pivot]):
            right-=1

        if (left>right): #엇갈렸다면 작은데이터와 피벗을 교체
            array[right], array[pivot] =array [pivot], array[right]
        else: #엇갈리지 않았다면 작은데이터와 큰데이터 교체
            array[left], array[right] =array[right], array[left]

        #분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right  +1 , end)

quick_sort(array, 0, len(array)-1)




#4. 계수정렬
#특정한 조건이 부합할때만 사용할수 있지만 매우 빠르게 동작함
#데이터 크기범위가 제한됨



array =[7,5,9,0,3,1,6,2,4,8]

#모든 범위를 포함하는 리스트 선언, 모든값은 0으로 초기화
count =[0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] +=1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): #리스트에 기록된 정렬 정보 확인/인덱스 0 부터 9까지 확인
    for j in range(count[i]):
        print(i,end=' ')





