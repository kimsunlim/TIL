

# Linear regression model 선형회귀모델 
#연속형 원인변수가 연속형 결과 변수에 영향을 미치는지를 분석하여 레이블 변수를 예측하기 위함


import pandas as pd 
data2= pd.read_csv('house_price.csv',encoding='utf-8')
X=data2[data2.columns[1:5]]
y=data2[['house_value']]



#분리
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test =train_test_split(X,y, random_state=42)

# 통계적 회귀모델에서는 정규화를 일반적으로 하지 않는다
#statmodel 적용 > 파이썬 통계분석 모델

import statsmodels.api as sm
x_train_new = sm.add_constant(X_train)
x_test_new =sm.add_constant(X_test)
x_train_new.head()


#훈련데이터
##sm.OLS 적용

multi_model = sm.OLS(y_train, x_train_new).fit()
print(multi_model.summary())

#R-squared확인 54%수준으로 회귀직선인 예측값과 실제값이 일치 


#테스트데이터
multi_model2=sm.OLS(y_test, x_test_new).fit()
print(multi_model2)

#설명력 56%
#x변수가 유의미함



##sckit-learn적용



import pandas as pd 
data2= pd.read_csv('house_price.csv',encoding='utf-8')
X=data2[data2.columns[1:5]]
y=data2[['house_value']]



#분리
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test =train_test_split(X,y, random_state=42)

#정규화
from sklearn.preprocessing import MinMaxScaler 
scaler=MinMaxScaler()

scaler.fit(X_train)
X_scaled_train=scaler.transfrom(X_train)
X_scaled_test =scaler.transform (X_test)



#사이킷런 모델적용
from sklearn.linear_model import LinearRegression

model= LinearRegression()
model.fit(X_scaled_train, y_train)
pred_train=model.predict(X_scaled_train)
model.score(X_scaled_train, y_train)

#54%  

pred_test =model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)


##RMSE 실제값과 예측값간에 전구간에 걸친 평균적인 오차 / 평균제곱근오차

import numpy as np
from sklearn.metrics import mean_squared_error 

MSE_train =mean_squared_error (y_train, pred_train)
MSE_test = mean_squared_error(y_test, pred_test)

print(np.sqrt(MSE_train))
print(np.sqrt(MSE_test))


#절대편균오차 MAE

from sklearn.metrics import mean_absolute_error 
mean_absolute_error(y_test, pred_test )
#43%

#평균제곱오차 MSE 실제값과 예측값의 차이 >>오차에 제곱을 한 오차 지표 ..제곱을해서 크다

from sklearn.metrics import mean_squared_error  
mean_squared_error(y_test, pred_test)

#평균절대 오차비율 MAPE> 실제값- 예측값 백분율 >> 시계열데이터에서 많이 사용

def MAPE(y_test, pred_test):
    return np.mean(np.abs((y_test-pred_test)/y_test)) *100 
MAPE(y_test,pred_test)

#30%


#평균오차비율 >0을 기주으로 실제값보다 예측값이 큰지 작은지>>MPE

def MAE (y_test, y_pred):
    return np.mean ((y_test-pred_test)/y_test) *100 
MAE(y_test, pred_test)

#-12%








