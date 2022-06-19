

#작업형 예제1
# alcohol이 상위 10번째 값으로 상위 1~10위의 범위의 값을 변경한 후
#speeding속도가 7이상의 음주수치 데이터들의 평균 산출


#풀이 
#1. alcohol 열을 내림차순으로 정렬후 data에 할당
#2.alcolhol을 상위 10번쨰 값을 추출하여 ten변수에 할당
#3.상위 10위의 범위의 값을 추출
#4. 수정된 데이터를 기반으로 speeding열이 7이상인 값을 result에 할당
#5. 평균 구하기 


import pandas as pd 
df = pd.read_csv('car_crash')

#내림차순으로 정렬 
data=df.sort_value(by=df.columns[2], ascending=False)##음주수치 열만 내림차순정렬
ten=data.iloc[9,2] #10번째 값 추출 (9번째 행 (10번째값)의 2번째열인 음주수치)

data.iloc[:10,2]=ten # 상위 1~10 추출 (2번째 열의) ten에 할당 하기 
result=data[(data['speeding']>=7)]
print(result['alcohol'].mean())




#작업형 예제2
#데이터 첫번쨰 행부터 70%까지의 데이터를 추출후 
#distance결측값을 distance의 중앙값으로 대체하고
#결측값 전처리 전과 후의 표준편차를 비교


#1. len 함수로 데이터의 79%까지 추출
#2. distance 결측값을 중아값으로 대체 
#3. 결측치 전의 distance열의 표준편차의 결측치 보정후  distance열의 표준편차를 출력

import pandas as pd 
import numpy as np

df= pd.read_csv('palnets')

len=int(len(df)*0.7)  ##len 함수 쓰면 %도 추출 가능!11
df= df[:len]  #전처리 전의 값
df2=df.copy() #전처리 후의 값

df2['distance']= df2['distance'].fillna(df2['distance'].median())
print('전처리 전 ',np.std(df['distance']))
print('전처리 후 ',np.std(df2['distance']))





#작업형 예제3
# preiod열의 이상치 IQR 기법으로 제거하여
#이상치들의 합을 계산


import pandas as pd 

df=pd.read_csv('planets')

Q25= df['orbital_period'].quantitle(0.25) #1사분위수 구하기
Q75= df['orbital_period'].quantitle(0.75) #3사분위수 구하기

IQR= Q75-Q25  #3사분위수 - 1사분위수  =IQR
min= Q25-IQR*1.5
max= Q75+IQR*1.5

df_outlier= df[(df['orbital_period']<=min)| (df['orbital_period']>=max) ]
#min 보다 작은값 곱하기 max보다 큰 값이 이상치임

print(df_outlier['orvital_period'].sum())





















