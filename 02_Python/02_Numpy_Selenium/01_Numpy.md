# Numpy

-  배열과 리스크의 차이점
- 배열 생성 다루는 기법
- 기술 통계
- 결과에 대한 분석하는 방법



- 넘파이의 배열은 모소 원소가 같은 자료형이어야한다
- resizing  X





- Vector(1차원-배열)-pandas(series)
- Matrix(2차원-행렬)-pandas(DataFrame)





### import numpy 

```python
import numpy as np

def aryInfo(ary):
    print('type:{}'.format(type(ary)))
    print('shape:{}'.format(ary.shape))
    print('demension:{}'.format(ary.ndim))
    print('type:{}'.format(ary.dtype))
    print("Arry Data:\n", ary)
```





## 1차원 배열 생성

- arry()

  ```python
  oneAry= np.array([0,1,2,3,4,5,6,7,8,9])
  aryInfo (oneAry)
  ```

- List vs Array 차이점 (Vector operation)

  ```python
  #1
  data=[0,1,2,3,4,5,6,7,8,9]
  data*2
  
  #2
  result=[]
  for d in data:
      result.append(d*2)
  result
  
  #3
  result2=[d*2 for d in data]
  result2
  
  ```

- 벡터 연산은 비교,산술,논리 연산을 포함하는 모든 수학연산에 적용됨

  ```python
  xAry= np.array ([1,2,3])
  xAry= np.array([10,20,30])
  
  
  2*xAry+yAry
  
  xAry == 2
  
  (xAry == 2)&(yAry > 20)
  ```

  



## 2차원 배열

- ndarray(N-dimensional Array)
- 2차원,3차원(다차원 배열 자료구조)
- 2차원 배열은 행렬(Matrix)
- list of list
- list of list of list



```python
# 2개의 행과 3개의 열을 가지는 배열을 만든다면
twoAry=np.array([[1,2,3],[4,5,6]],dtype=np.float64)
aryInfo(twoAry)


#행의 개수,열의 개수
print(len(twoAry)) 
print(len(twoAry[0]))
print(len(twoAry[1]))
```





## 3차원 배열 생성

```python
#2,3,4

threeAry=np.array([[[1,2,3,4],
                  [5,6,7,8],
                   [9,10,11,12]],
                  [[11,12,13,14],[15,16,17,18],
                  [19,20,21,22]]]  )
               
aryInfo(threeAry)




print('dept',len(threeAry))
print('row',len(threeAry[0]))
print('row',len(threeAry[1]))
print('row[0] col',len(threeAry[0][0]))





typeChange=threeAry.astype(np.float64)
aryInfo(typeChange)


indexAry =np.array([1,2,3,4,5,6,7])
aryInfo(indexAry)
```

```python
aryInfo(twoAry)
# twoAry indexing
# 첫번째 행의 첫번째 열
print(twoAry[0],[0])

# 첫번째 행의 두번째 열
print(twoAry[0],[1])

# 마지막행의 마지막 열
print(twoAry[-1],[-1])


slicingAry =np.array([[1,2,3,4],[5,6,7,8]])
aryInfo(slicingAry)

#첫번째 행의 전체
print(slicingAry[0, :])
#두번째 열의 전체
print(slicingAry[:  ,1])

#두번째 행의 두번째 열부터 끝까지
print(slicingAry[1,1:])


m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])
aryInfo(m)

#이 행렬에서 값7을 인덱싱한다.
print(m[1,2])

#이 행렬에서 값14을 인덱싱한다.
print(m[2,4])

#이 행렬에서 배열[6,7] 슬라이싱한다.
print(m[1,1:3])

#이 행렬에서 배열[7,12] 슬라이싱한다..
print(m[1:,2])

#이 행렬에서 배열[[3,4],[8,9]] 슬라이싱한다..
print(m[0:2,3:5])
```



```python
#1
arr = np.array([0,1,2,3,4,5,6,7,8,9])
aryInfo(arr)
idx_arr=ap.array([True,False,True,False,True,False,True,False,True,False])
print(arr[idx])

arr%2==0

#2
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

aryInfo(x)
#이배열에서 3의 배수를 찾아라
print(x[x %3 == 0])
#이배열에서 4로 나누면 1이 남는 수를 찾아라
print(x[x% 4 == 1])
#이배열에서 3으로 나누면 나누어지고 4로 나누면 1로 남는 수를 찾아라
print(x[(x %3 == 0)&(x%4 ==1)])

#3
#인덱스 배열을 전달하여 배열 요소를 참조해보자
fancyAry=np.arange(0,12,1).reshape(3,4)
aryInfo(fancyAry)

fancyAry[2,2]  #10
fancyAry[1:2,2]#6
fancyAry[1:2, 1:2]#5
```





## 배열 변형 (타입,형태)

```python
x= np.array([1,2,3], dtype='U')
aryInfo(x)

x[0]+x[1] #12
```

- zeros, ones
- zeros_like,ones_like
- empty
- arange
- linspace,logspace

- zeros: 크기가 정해져있고 모든값이 0인 배열을 생성하려면

  ```python
  #1
  z=np.zeros(5)
  aryInfo(z)
  
  z=np.zeros((2,3),dtype='i')
  aryInfo(z)
  
  #2
  o=np.ones((2,3,4),dtype='i8')
  aryInfo(o)
  
  #3
  o_like=np.ones_like(o,dtype='f')
  aryInfo(o_like)
  
  #4
  z_like =np.zeros_like(z)
  aryInfo(z_like)
  
  #5
  e=np.empty((4,3))
  aryInfo(e)
  
  -a=np.arange(10)   # 0....n-1
  
  a=np.arange(3,21,2)
  aryInfo(a)
  
  ```

  ![numpy_dtype_img](C:\Users\user\Desktop\09_Numpy.assets\numpy_dtype_img.png)