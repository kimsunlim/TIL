# Python



### 1. 수와 계산

- 기본

```python
print(10+5) #10과 5를 더한 값을 출력해라
print(10*5)
print(10/5)


```



- 수학적인 작업할때_ import math

```python
import math

print(math.ceil(2.2))  # 괄호 안의 숫자를 올림 3
print(math.floor(2.2)) # 괄호 안의 숫자를 내림 2
print(math.pow(2,10))  #2의 10승  1024
print(math.pi)         # 파이값 
    
```





### 2. 문자와 데이터 타입

- 문자열 string

```python
print('Hello') # Hello 출력
print("Hello") # Hello 출력
print("Hello 'world'") #Hello'world' 출력
```



- 문자열 제어

```python
print('Hello'+'World')  # Helloworld 출력
print('Hello '*3)       # Hello Hello Hello출력
print('Hello'[0])       #[]:위치값 출력, 첫번째 값 H 출력
print('Hello'[1])       # 두번째 값 e 출력

```





- 문자열 제어2

```python 
print('hello world'.capitalize())  # Hello world 첫문자 대문자로 출력
print('hello world'.upper())     #HELLO WORLD 모두 다 대문자로 출력
print('hello world'.__len__())    #11 문자열 개수
print(len('hello world'))		  #11 문자열 개수
print('Hello world'.replace('world', 'programming')) #Hello programming/ world를 programming로 대체
```









### 3. 변수

- 변수의 기본 문법

```python
x=10			# 변수 정의 
y=5
print(x+y)


title= "python"
print("Title is"+title)  #Title is python

```



- 문자열에서 변수

```python
name="김선림"
print("안녕하세요."+name+"님")  #안녕하세요 김선림님  출력
print(name +"님 파이썬 화이팅 하세용") # 김선림님 파이썬 화이팅 하세용 
```





- 수 계산에서 변수

```python
donation =200
student =10
sponstor =100

print((donation*student)/sponsor)  #변수가 계산되어 20출력
```

