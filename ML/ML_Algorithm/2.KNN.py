import warnings 
warnings.filterwarnings('ignore')

import pandas as pd
data=pd.read_csv['breast-cancer-wiscon.csv',encoding='utf-8']

X=data[data.columns[1:10]]
y=data[['Class']]


from sklearn.model_selection import train_test_split 

X_train,X_test, y_train,y_test =train_test_split(X,y,stratify=y, randomstate=42)

# 정규화

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
X_scaled_trian=scaler.transform(X_train)
X_scaled_test =scaler.transform(X_test)



####KNN 분류
#분류모델적용

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()

model.fit(X_scaled_train, y_trian) #분류모델 훈련시키고
pred_trian= model.predict(X_scaled_train) #분류예측을 한후
model.score(X_scaled_trian,y_trian) # 휸련데이터의 정확도를 구해본다!

##테스트 데이터 분류예측
pred_test=model.predict(X_scaled_test)
model.score(X_scaled_test, y_test)


## 오차행렬 검토

#훈련데이터
from sklearn.metrics import confusion_matrix 
confusion_train = confusion_matrix(y_trian, pred_train) #분류 예측한 x으로 구해야함
print('훈련데이터 오차행렬:\n',confusion_train)

#테스트데이터
confusion_test= confusion_matrix(y_test,pred_test)
print('훈련데이터 오차행렬:\n',confusion_test)



## 정밀도와 재현율 확인

#훈련데이터
from sklearn.metrics import classification_report
cfreport_train=clssification_report(y_trian,pred_trian)
print('분류예측 리포트:\n', cfreport_train)


cfreport_test=classification_report(y_test,x_sclaed_test)
print('분류예측 리포트:\n', cfreport_test)



##Grid search

param_gird={'n_neighbors':[1,3,5,7,9,11]}

from sklearn.model_selection improt GridSearchCV
grid_search=GridSearchCV(KNeighborsClassifier(),param_gird, cv=5)
gird_sarch.fit(X_scaled_train,y_train)


print('bestparameter:{}'.format(grid_search.best_params_))
print('bestscore:{:4f}'.format(grid_search.best_score_))
print('testsetScore:{:4f}'.format(grid_search.score(X_scaled_test,y_test)))




#Random search

from scipy.stats import randint
param_distribs={'n_neighbors:'randint(low=1,high=20)}

from sklearn.model_selection import RadomizedSearchCV
random_search=RandoizedSearchCV(KNeighborsClassifier(),param_distributions=param_distibs, n_iter=20,cv=5)
random_search.fit(X_scaled_train, y_trian)


print('bestparameter:{}'.format(random_search.best_params_))
print('bestscore:{:4f}'.format(random_search.best_score_))
print('testsetScore:{:4f}'.format(random_search.score(X_scaled_test,y_test)))



### KNN 회귀


#데이터준비
data2=pd.read_csv('house_price.csv',encoding='utf-8')
X=data2[data2.columns[1:5]]
y=data2[['house_value']]

from sklearn.model_selection import train_test_split 

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42)



#정규화

from sklearn.preprocessiong import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(X_train)
X_scaled_trian= scaler.transform(X_train)
X_scaled_test =scaler.transfrom(X_test)

#KNN회귀 모델 적용

from sklearn.neighbors import KNeighbprsRegressor
model=kNeighborsRegressor()
model.fit(X_scaled_train,y_trian)
pred_trian=model.predict(X_scaled_train)
model.score(X_scaled_trian,y_train)

pred_test=model.predict(X_scaled_test)
model.score(X_sclaed_test,y_test)



#회귀모델 평가지표 RSME (root mean squared error)

import numpy as np

from sklearn.metrics import mean_squared_error

mse_train =mean_squared_error(y_trian,pred_train)
mse_test = mean_squared_error(y_test,pred_Test)

print('훈련데이터 rsme:',np.sqrt(mse_trian))
print('훈련데이터 rsme:',np.sqrt(mse_test))


#grid search

grid_search={'n_neighbors':[1,3,5,7,9,11]}

from sklearn.model_selection import GridSearchCV

grid_search=GridSearchCV(KNeighborsRegressor(),param_grid, cv=5)
gird_search.fit(X_scaled_train,y_train)


#Random search

random_dsistribs={'n_neighbors:'randint(low=1, high=20)}

from sklearn.model_selection import RandomizedSearchCV 

random_search=RandomizedSearchCV(KNeighborsRegressor(),param_distibutions=param_distirbs, n_iter=20,cv=5)

random_search.fit(X_scaled_train,y_train)









































