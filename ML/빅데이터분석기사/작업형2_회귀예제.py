##작업형 2 회귀 문제

# 성능이 우수한 예측모형을 구축하기 위해서 적합한 데이터 처리 
#rmse,mae평가지표
#종속변수 mpg

import seaborn as sns
import pandas as pd 
import numpy as np 

df=sns.load_datset['mpg']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(df,df['mpg'],random_state=42)

X_train=X_train.drop(['mpg'],axis=1)
X_test=X_test.drop(['mpg'],axis=1)

print(X_train.head())

#1. 결측치 확인 
print(X_train.isnull().sum())

#중앙값 대체 
X_train['horespower']=X_train['horespower'].fillna(X_train['horepower'].median())
X_test['horespower']=X_test['horespower'].fillna(X_test['horepower'].median())


#2. 라벨 인코딩 

from sklearn.preprocessing import LabelEncoder
label=['origin','name']

X_train[label]=X_train[label].apply(LabelEncoder().fit_transform)
X_test[label]=X_test[label].apply(LabelEncoder().fit_transfom)

#3. 타입변환 ,더미 

df.dtypes

category=['origin']

for i in category:
    X_train[i]=X_train[i].astype('category')
    X_test[i]=X_test[i].astype('category')
    
X_train= pd.get_dummies(X_train)
X_test= pd.get_dummies(X_test)


#4. 파생변수

X_train['horspower_qcut']=pd.qcut(X_train['horsepower'],5,labels=False)
X_test['horspower_qcut']=pd.qcut(X_test['horsepower'],5,labels=False)


#5. 스케일링

from sklearn.preprocessing import MinMaxScaler
scaler=['displace','weight','horsepower']

min=MinMaxScaler()

min.fit(X_train[scaler])
X_train[scaler]=min.transform(X_train[scaler])
X_test[scaler]=min.transform(X_test[scaler])


#6. 데이터셋 분할

#독립변수, 종속변수, 테스트 사이즈
X_train,X_valid,y_train, y_valid = train_test_split(X_train,y_train, test_size=0.2, random_state='42')
print(X_train.shape)



#7.회귀 모형학습 

#선형회귀, 랜포회귀 사용
#앙상블 스태킹

from sklearn.linear_model import LinearRegression
model1=LinearRegression()
model1.fit(X_train,y_train)

pred1=model1.predict(X_valid)

from sklearn.ensemble import RandomForestRegressor 
model2= RandomForestRegressor()
model2.fit(X_train,y_train)
pred2= model2.predict(X_valid)


#8. 앙상블 스태킹 적용 

from sklearn.ensemble import StackingRegressor
estimators=[('lr',model1),('rf',model2)]

model3=StackingRegressor(estimators=estimators, final_estimators = RandomForestRegressor())
model3.fit(X_train,y_train)
pred3=model3.predict(X_valid)



#9. 평가 지표 

from sklearn.metrics import mean_squared_error
rmse=mean_squared_error()

print('선형회귀mse', rmse(y_valid,pred1))
print('선형회귀mse', rmse(y_valid,pred2))
print('선형회귀mse', rmse(y_valid,pred3))


print('선형회귀rmse', np.sqrt(rmse(y_valid,pred1)))
print('선형회귀rmse', np.sqrt(rmse(y_valid,pred2)))
print('선형회귀rmse', np.sqrt(rmse(y_valid,pred3)))


#10. 하이퍼파라미터 튜닝 

from sklearn.model_selections import GridSearchCV 
parameters={'n_estimators':[50,100],'max_depth':[4,6]}
model4=RandomForestRegressor()

clf=GridSearchCV(estimators=model4, param_grid=parameters, cv=3)
clf.fit(X_train,y_train)

print('최적',clf.best_params_)


#11. 데이터 저장

result= pd.DataFrame(model2.predict(X_test))
##모델2를 예측해서 넣기 ! 
result=result.iloc[:,0]

pd.DataFrame({'id':X_test.indes, 'result':result}).to_csv('oo4.csv',index=False)

check=pd.read_csv('004.csv')
check.head()













