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

