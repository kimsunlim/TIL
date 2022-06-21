##회귀분석

#성능이 우수한 얘측 모형 구축하기 위해 적절한 데이터 전처리
#RMSE평가지표
#종속변수 mpg

import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df=pd.read_csv('mpg')
X_train, X_test, y_train, y_test = train_test_split(df, df['mpg'],test_size=0.2, random_state=42)
X_train=X_train.drop(['mpg'],axis=1)
X_test=X_test.drop(['mpg'],axis=1)


#결측치 처리
print(X_train.isnull().sum())

X_train['horsepower']= X_train['horsepower'].fillna(X_train['horsepower'].median())
X_test['horsepower']= X_test['horsepower'].fillna(X_test['horsepower'].median())


#라벨인코딩
#문자로 된걸 숫자로

from sklearn.preprocessing import LabelEncoder
label=['origin','name']


X_train[label]=X_train[label].apply(LabelEncoder().fit_transform)
X_train[label]=X_test[label].apply(LabelEncoder().fit_transform)

print(X_train.head())

#카테고리 타입변환, 더미처리

category=['origin']

for i in category:
    X_train[i]=X_train[i].astype['category']
    X_test[i] = X_test[i].astype['category']

X_train=pd.get_dummies(X_train)
X_test=pd.get_dummies(X_test)

# 파생변수  생성
#연속형을 만들어야함 ,5구간으로 나누기

X_train['horsepower_qcut']=pd.qcut(X_train['horsepower'],5, labels=False)
X_test['horsepower_qcut']=pd.qcut(X_test['horsepower'],5, labels=False)


#스케일링

from sklearn.preprocessing import MinMaxScaler

scaler=['display','horsepower','weight']

min=MinMaxScaler()
min.fit(X_train[scaler])

X_train[scaler]= min.transform(X_train[scaler])
X_test[scaler]= min.transform(X_test[scaler])


#데이터 분리

X_train, X_valid, y_train, y_valid=train_test_split(X_train,y_train,test_size=0.2, random_state=42)

print(X_train.shape)

##모형학습
from sklearn.linear_model import LinearRegression
model1=LinearRegression()
model1.fit(X_train, y_train)
pred1=model1.predict(X_valid)

from sklearn.ensemble import RandomFoestRegressor
model2= RandomForestRegressor
model2.fit(X_train, y_train)
pred2=model2.predict(X_valid)

##앙상블 스태킹 학습

from sklearn.ensemble import StackingRegressor
estimaors=[('lr',model1),('rf',model2)]
model3=StackingRegressor (estimators=estimators, final_esimator=RandomForestRegressor())
model3.fit(X_train,y_train)
pred3=model3.predict(X_valid)

# 성능 평가

from sklearn.metrics import mean_squared_error

print('선형회귀 mse', mean_squared_error(y_valid,pred1))

print('선형회귀 rmse', np.sqrt(mean_squared_error(y_valid,pred1)))

##모델 튜닝

from sklearn.model_selections import GridSearchCV
parameters={'n_estimators':[50,100], 'max_depth':[4,6]}
model4=RandomForestRegressor()
clf=GridSearchCV(estimator=model4, param_grid=parameters, cv=3)
clf.fit(X_train, y_train)

print('최적', clf.best_params)

# 데이터 저장
result=pd.DataFrame(model2.predict(X_test))
result=rseult.iloc[:,0]

pd.DataFrame({'id':X_test.index, 'result':result}).to_csv('0040.csv',index=False)
