## 이진 탐색
# 정렬 되어 있는 리스트를 빠르게 탐색하는것!! 이떄, 탐색범위가 절반씩 줄어듬



#이진 탐색 소스 코드 구현(재귀함수)

def binary_search(array, target,start,end):#배열정보, 찾고자하는 타겟, 탐색시작과 끝점
    if start>end: #시작점이 끝점보다 크면 탐색하고자 하는게 없다는 의미
        return None
    mid=(start+end)//2  # 그외의 경우엔 시작점+끝점 //2로 중간점 설정가능

    #찾은 경우 중간점 인덱스 반환
    if array[mid]== target:   #같으면 해당값 찾은 것
        return  mid

    #중간점의 값보다 찾고자 하는값이 작은경우 왼쪽확인
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)#끝점을 중간점 왼쪽으로 반환하여 다시 탐색하도록 설정

    #중간점의 값보다 찾고자하는 값이 큰 경우 오른쪽확인
    else:
        return binary_search(array, target,mid+1,end)


    #n(원소의 개수)과 target(찾고자하는 값)을 입력받기
    n,target = list(map(int,input().split()))

    #전체원소 입력받기
    array=list(map(int,input().split()))

    #이진 탐색 수행 결과 출력
    result=binary_search(array,target,0,n-1)
    if result ==None:
        print('원소가 존재하지 않습니다')
    else:
        print(result+1)


    ##파이썬 이진탐색 라이브러리
    #bisect_left(a,x) :정렬된 순서를 유지하면서 배열 a에 x를 삽입할때 가장 왼쪽 인덱스 반환
    #bisect_right(a,x):정렬된 순서를 유지하면서 배열a에 x를 삽입할때 가장 오른쪽 반환환






#Q1.  떡볶이 떡만들기

#탐색범위가 클때는 이진탐색 써야함


#떡의 개수(n)와 요청한 떡의 길이(m)을 입력

n,m =list(map(int,input().split()))
array=list(map(int,input().split()))

#이진 탐색을 위한 시작점, 끝점 설정
start =0
end=max(array)  #가장 긴떡길이가 end값

#이진 탐색 수행(반복적)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2 #중간값
    for x in array:
        #잘랐을때 떡의 양 계산
        if x> mid:
            total +=x-mid  #잘린떡 담기
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분탐색)
    if total <m:
        end=mid-1

    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분탐색)
    else:
        result =mid #최대한 덜 잘랐을떄가 정답이므로 result에 기록
        start=mid +1



#Q2.  정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left,bisect_right

#값이 (left_value,right_value)인 데이터개수를 반환하는 함수
def count_by_range(array, left_value,right_value):
    right_value=bisect_right(array,right_value)
    left_value=bisect_left(array,left_value)
    return right_value-left_value

n,x =list(map(int,input().split()))
array=list(map(int,input().split()))

#값이 [x,x]벙위에 있는 데이터 개수 계산
count =count_by_range(array,x,x)

#값이x인 원소가 존재하지 않는다면
if count ==0:
    print(-1)

#값이 x인 원소가 존재한다면
else:
    print(count)



























