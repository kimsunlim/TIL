
#백준 3053 택시 기하학

#유클리드 기하학과 택시기하학 각각 출력




import math

r= int(input()) #반지름 입력값 받기
print(r*r*math.pi) #유클리드기하학 원의 넓이 : 반지름*반지름*원주율
print(2*r*r) #택시기하학 원의 넓이 : 2*반지름*반지름


#택시기하학
#원의 모습이 마름모꼴 정사각형이 된다.
#r*r*2하면 마름모꼴을 구할 수 있다.