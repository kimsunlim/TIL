
#작업형 예제 1

##1번
#1. 데이터셋의 f5컬럼을 기준으로 상위 10개의 데이터를 구하고.
# f5컬럼 10개 중 최소값으로 데이터를 대체한 후 
# age컬럼에서 80 이상인 데이터의 f5컬럼 평균값 구하기



#메모 
#1. f5컬럼 기준으로 정렬하고 상위 10개만 추출 
#2. f5의 최솟값구하기
#3.f5열개행을 최솟값으로 대체
#4. age에서 80 아상인 데이터는 f5평균값으로 대체하기 



import pandas as pd 
df=pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.head()

#1. f5컬럼 기준으로 정렬하고 상위 10개만 추출 

df=df.sort_values('f5', ascending=False)  #ascending  주의!!!
df.head(10)


#2. f5의 최솟값구하기
min=df['f5'].min()
#min=91.297791


#3.f5열개행을 최솟값으로 대체

df['f5'][:10]=min


#4. age에서 80 아상인 데이터는 f5평균값으로 대체하기 

print (df[df['80']>=80]['f5'].mean())




##2번
#2. 데이터셋의 앞에서 순서대로 70%만 활용해서 
# f1컬럼의 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고 > 결측치 채우기 전후의 표준편차 구하기
# 두 표준 편차 차이 계산 



#메모
#1. 데이터셋 앞에서 부터 70% 추출 
#2. f1컬럼의 결측치를 확인
#3.결측치 채우기전 f1 표준편차 
#4. 결측치 채운후 중앙값 대체, 표준편차
#5. 표준편차 구하기 


import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')




#1. 데이터셋 앞에서 부터 70% 추출 
df70=df.iloc[:70]



#2. f1컬럼의 결측치를 중앙값으로 대체 
df70.isnull().sum()



#3.결측치 채우기전 f1 표준편차 
std1= df70['f1'].std()



#4. 결측치 채운후 중앙값 대체, 표준편차
df70['f1']= df70['f1'].fillna(df70['f1'].median())

std2=df70['f1'].std()



#5. 표준편차 구하기
print(std1-std2)



##3번 
#3. 데이터셋의 age컬럼의 이상치를 더하시오
#단 평균으로부터 표준편차 *15을 벗어나는 영역이 이상치임

#age의 min값과 max값을 구해서 빼준 iqr값구하기 

import pandas as pd 
import numpy as np 
df=pd.read_csv('abc.csv')



# 표준편차*15, 평균값 구하기
std=np.std(df['age'])*1.5  
mean=df['age'].mean()


#최소, 최대 이상치 구하기

min_out= mean-std
max_out=mean+std 

print(min_out,max_out)

#이상치 age합 

df[(df['age']>max_out)|(df['age']<min_out)]['age'].sum()






##4번 
#https://www.kaggle.com/code/agileteam/tutorial-t1-python

# 자동차 데이터 셋에서 qsec 컬럼을 민맥스 스ㅔ이로 변환후 0.5보다 큰값을 가지는 레코드 수?


#민맥스 적용
#훈련데이터에 적용하는게 아니라
#minmax_scale패키지 써줄것 !!1

import pandas as pd 
from sklearn.preprocessing import minmax_scale

df['qsec']=minmax_scale(df['qsec'])

print((df['qsec']>0.5))  #true더함
print(len(df[df['qsec']>0.5])) #데이터 수 구함  





##5번 
#첫번째 데이터 부터 순서대로 50:50으로 데이터를 나누고, 앞에서 부터 50%의 데이터는 f1컬럼을 a그룹의 중아값으로 채우고
#뒤에서 부터 50%데이터는 f1컬럼을 b그룹의 최댓갑으로 채운후.
#a그룹과 b그룸의 표준편차 합을 구하시오 
#단 소수점 첫째까지 자리만 구하기!


#메모 
# 50:50으로 데이터 a,b그룹 나누기 
# a그룹은 f1컬럼의 중앙값
# b그룹은 f1컬럼의 최댓값으로 채우기

#a와 b의 표준편차 합 구하기




import pandas as pd 
df=pd.read_csv('abc.csv')

# 50:50으로 데이터 a,b그룹 나누기 
dfa=df.iloc[:50]
dfb=df.iloc[50:]


# a그룹은 f1컬럼의 중앙값
dfa.loc[:,'f1']=dfa['f1'].fillna(dfa['f1'].median())

# b그룹은 f1컬럼의 최댓값으로 채우기

dfb.loc[:,'f1']=dfb['f1'].fillna(dfb['f1'].max())


#a와 b의 표준편차 합 구하기

print(round(dfa['f1'].std()+dfb['f1'].std(),1))







##6.
#f4컬럼 기준으로 내림차순 정렬과 , f5기준으로 오름 차순 정렬을 순서대로 다중조건 정렬하고나서
#앞에서 부터 10개의 데이터중 f5컬럼의 최소값을 찾고, 
# 이 최소값으로 앞에서 부터 10개의 'f5'컬럼 데이터를 변경함
#그리고 f5의 평균값을 계산함 


#단 소수점 둘째자리까지 출력



df=df.sort_values(['f4','f5'],ascending=[False,True]).reset_index(drop=True)


df.iloc[:10,7]=df['f5'][:10].min()
print(round(df['f5'].mean(),2))


##7.age컬럼의 IQR방식을 이요한 이상치 수와 표준 편차 *1.5방식을 이용한 이상치 수 합을 구해라

Q1=df['age'].quantile(0.25)
Q3=df['age'].quantile(0.75)

#IQR방식
IQR=Q3-Q1
min=Q1-1.5*IQR
max=Q3+.5*IQR

out1= sum((df['age']<min)|(df['age']>max))


#표준편차 방식 
std=df['age'].std()*1.5 
mean=df['age'].mean()

min_out=mean-std
max_out=mean+std

out2= sum((df['age']< min_out)|(df['age']> max_out))




print(out1+out2)








