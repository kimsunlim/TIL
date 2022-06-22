# 작업형1 _4예졔


##1번
#이상치를 찾아라

#IQR활용해서   FARE컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오




#메모
#데이터 불러오기 
#1사분위구하기
#3사분위 구하기
#IQR구하기
#fare컬럼 이상치 구하기
#이상치 데이터의 여성수 구하기




# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
df = pd.read_csv('../input/titanic/train.csv')


#1사분위구하기
Q1=df['Fare'].quantile(0.25)

#1사분위구하기
Q3=df['Fare'].quantile(0.75)

IQR=Q3-Q1

print(Q1-1.5*IQR, Q3+1.5*IQR)


#이상치 구하기

out1= df[df['Fare']<(Q1-1.5*IQR)]
out3= df[df['Fare']<(Q3+1.5*IQR)]

len(out1),len(out3)

#이상치 데이터에서 여성수 구하기 

print(sum(out3['sex'] =='female'))







##2번
#이상치를 찾아라
# 주어진 데이터에서  이상치를 찾고(소수점 나이) 
#올림,내림,버림(절사 ) 했을때 3가지 모두 이상치 age평균을 구한다음 더해라





#메모
#소수점 데이터 찾기
#1. 이상치 찾기 
#2. 이상치 올림, 내림, 절삭 찾기(age)
#3. 3변수의 평균구한다음 더하기


import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.head()


#소수점 데이터 찾기 
df=df[(df['age'] - np.floor(df['age'])) !=0]


# 이상치 올림, 내림, 절삭 찾기(age)

age=np.ceil(df['age']).mean()
floor=np.ceil(df['age']).mean()
trunc=np.trunc(df['age']).mean()

print(age+floor+trunc)




##3번 
# 1데이터의 f4를 기준으로 3데이터의 f4값 기준으로 병합하고 
# 병합한 데이터에서 r2의 결측치를 제거한 다음, 앞에서 부터 20개 데이터를 선택하고 
#f2컬럼 합을 구해라 


##merge 함수 쓰는거 외우기!!!

# 라이브러리 및 데이터 로드
import pandas as pd
b1 = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
b3 = pd.read_csv("../input/bigdatacertificationkr/basic3.csv")

b1.head()
b3.head()


# 데이터결합!! f4값 기준으로 병합
df= pd.merge(left=b1, right=b3, how="left", on="f4")
df.head()


#결측치 제거 
df.isnull().sum()

df=df.droupna(subset=['r2'])

#인덱스 리셋 
df=df.reset_index()

#앞에서 부터 20개 선택후 합 
print(df.iloc[:20]['f2'].sum())


