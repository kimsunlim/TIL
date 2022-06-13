
## 데이터 탐색과 데이터 정제

## 1. 단변량 데이터 탐색

import pandas as pd 
data= pd.read_csv('Ex_CEOSalary.csv', encoding='utf-8')

#데이터 정보
data.info()

#데이터 5개 케이스보기
data.head()


##매출과 수익이 연봉에 미치는 영향은?
#매출과 수익이 독립변수인 특성치, 연봉은 종속변수 레이블이 됨

## industry 변수는 범주형임 
#변수별 범주의 빈도 확인
data['industry'].value_counts()

#범주라벨링
data['industry']= data['industry'].replace([1,2,3,4],['s','i','f','o'])
data['industry'].value_counts()

##기술통계량 확인
data.describe()
#평균과 중위수가 일치할수록 이상치가 적은 데이터임!


##왜도 
data.skew()
##첨도
data.kurtosis()


## 2.이변량 데이터 탐색
## 두변수 간의 탐새도 필요함 


#corr()함수로 상관계수 파악 가능
data.corr()


#디폴트를 지정하지 않으면 피어슨으로 적용됨
data.corr(method='pearson')
data.corr(method='spearman')
data.corr(method='kendall')


import matplotlib.pyplot as plt 
plt.scatter(data['sales'], data['salary'],alpha=0.5)
plt.show()

##범주별 존속변수의 기술 통계량을 확인하고자 한다면 
data.groupby('industry')[['salary']].describe()



##3. 이상치처리
#분석 전에 반드시 해결해야함! 

#이상치 시각적으로 파악 > 상자수염도표 
data.boxplot(column='salary',return_type='both')

#이상치를 판단하는 명쾌한 기준은 없다. 분석자의 주관적인 판단에 의해 제거한다
#IQR기준으로 이상치 제거해보기

#IQR값 찾기 =671
Q1_salary = data['salary'].quantile(q=0.25)
Q3_salary = data['salary'].quantile(q=0.75)

IQR_salary =Q3_salary-Q1_salary

#IQR의 1.5배보다 큰값과 작은값 제거하기 그러고나서 새로운 변수에 할당

data_IQR= data[(data['salary']<Q3_salary+IQR_salary*1.5) & 
               (data['salary']>Q1_salary-IQR_salary*1.5)]
data_IQR['salary'].hist()


##이번엔 sales변수 이상치 제거 
#IQR값은 4966
Q1_sales= data['sales'].quantile(q=0.25)
Q3_sales= data['sales'].quantile(q=0.75)
IQR_sales =Q3_sales-Q1_sales


#이상치제거후 data_IQR할당>sales와 salary이상치 제거

data_IQR = data[(data['sales']<Q3_sales + IQR_sales*1.5)
                &(data['sales']>Q1_sales-IQR_sales*1.5)
                &(data['salary']<Q3_salary+IQR_salary*1.5)
                &(data['salary']>Q1_salary-IQR_salary*1.5)]
data_IQR['sales'].hist()




## 4. 변수변환
# 이상치를 제거하지 않은 원데이터를 변환함 

#로그 변환 
import numpy as np
data['log_salary'] = np.log(data['salary'])
data['log_sales'] = np.log(data['sales'])
data['log_roe'] = np.log(data['roe'])

data.head()
data.corr()

#제곱근변환ㄳ

data['sqrt_salary'] = np.sqrt(data['salary'])
data['sqrt_sales'] = np.sqrt(data['sales'])
data['sqrt_roe'] = np.sqrt(data['roe'])


data.head()
data.corr()


#변환만으로도 이상치 영향 크게 줄일수 있음

###5. 결측치 처리

import pandas as pd 
data= pd.read_csv('Ex_Missing.csv')
data



#결측치 아닌값반환 
data.notnull()

#결측치 확인
pd.isnull(data)
data.isnull()
data.isnull().sum()
data['salary'].isnull().sum()

#행별 결측치 확인
data.isnull().sum(1)

data['missing']=data.isnull().sum(1)


#결측값 제거 

#결측값 있는 행제거 
data_del_row = data.dropna(axis=0) #가로축 

#결측값 있는 열제거 
data_del_col=data.dropna(axis=1)#열제거 

#결측값있는 특정 행/열제거 
data[['salary']].dropna() #행

data[['salary']].dropna(axis=1) #열

##결측값 대체 

#1) 특정값으로 대체 
#0으로 대체
data_0 = data.fillna(0)

data_missing= data.fillna('missing')

#결측값을 앞의 변수로 대체 
data_ffill= data.fillna(method='ffill')
data_ffill= data.fillna(method='pad')
#뒤의 변수로 대체
data_ffill= data.fillna(method='backfill')
data_ffill= data.fillna(method='bfill')

#2) 평균으로 대체
data_mean=data.fillna(data.mean())
data_median =data.fillna(data.median())
data_max =data.fillna(data.max())

#변수의 평균값으로 대체
data_other_mean =data.fillna(data.mean()['salary'])

#3) 다른 변수값으로 대체 
import numpy as np 

data2=data.copy()
data2['sales_new'] =np.where(pd.notnull(data2['sales'])==True, data2['sales'], data2['salary'])

#4) 집단 평균값으로 대체 
#특정 변수의 그룹별 평균으로 대체 
#산업별 평균으로 결측값 대체 

data.groupby('industry').mean()

#람다로 편균으로 대체한다는 함수 생성
fill_mean_func= lambda g: g.fillna(g.mean())
data_group_mean=data.groupby('industry').apply(fill_mean_func)


#분석자가 설정한 값으로 
fill_values={1:1000, 2:2000}
fill_func = lambda d: d.fillna(fill_values[d.name])

data_group_value=data.groupby('industry').apply(fill_func)

#보간법,평균, 특정문자

missing_value={'salary':data.salary.interpolate(),
               'sales':data.sales.mean(),
               'roe':'missing'}

data.fillna(missing_value)



###실전문제 
import pandas as pd 
data= pd.read_csv('house_raw.csv')

data.head()
data.describe()


#선형회귀 적용 

X=data[data.columns[0:5]]
y=data[['house_value']]

#훈련데이터와 테스트데이터셋 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y, stratify=y,random_state=42)

#정규화 특성치의 단위를 동일하게 만듬
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()
scaler.fit(X_train)
X_scaler_train=scaler.transform(X_train)
X_scaler_test=scaler.transform(X_test)


#모델적용
from sklearn.linear_model import LinearRegression 
model=LinearRegression()
model.fit(X_scaler_train,y_train)


pred_train=model.predict(X_scaler_train)
model.score(X_scaler_train, y_train)
#정확도 55% > 훈련데이터의 정확도, 설명력 

pred_test =model.predict(X_scaler_test)
model.score(X_scaler_test)
#-2544 음수가 나왔는데 말도 안되결과 설명력은 0~1사이여야함

##데이터 정제를 위한 세부검토
#0.6이상의 큰값들이 존재해서 0.6 미만의 값 추출
data_bedroom =data[data['bedrooms']<0.6]

#0.6이상의 값확인
data_bedroom2=data[data['bedroom']>=0.6]
print(data_bedroom2['bedroom'].value_counts())

data_households2 =data[data['households']>=10]

data_room2 =data[data['room']>=20]

##정제데이터셋 생성
new_data=data[(data['bedrooms']<0.5) &(data['households']<7)&(data['room']<12)]

##선형회귀 모델 적용

#1. 특정데이터셋 레이블 데이터셋 나누기
X=new_data[new_data.columns[0:5]]
y=new_data[['house_value']]

#2. 트레인과 테스트데이터셋 구분
from sklearn.model_selection import train_test_split
X_train, x_test, y_train,  y_test=train_test_split(X,y,random_state=42)

#3.데이터 정규화
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()
X_scaler_train=scaler.transform(X_train)
X_scaler_test=scaler.transform(X_test)

#선형모델 적용
from sklearn.linear_model import LinearRegression 
model=LinearRegression()
model.fit(X_scaler_train,y_train)
pred_train= model.predict(X_scaler_train)
model.score(X_scaler_train, y_train)


##잘 정제되 ㄴ최종데이터 csv로 저장 
new_data.to_csv('house_price.csv',index=False)
