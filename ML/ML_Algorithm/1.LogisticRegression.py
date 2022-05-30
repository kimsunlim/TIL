
##Logistic Regression

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

data = pd.read_csv('breast-cancer-wiscionsin.csv',encoding='utf-8')

#특성치와 범주 데이터 분류
X=data[data.columns[1:10]]  #특성치
y=data[["Class"]]    #레이블


#트레인과 테스트셋 분리!! 기본 디폴트 비율 7:3으로 나누고 y범주의 비율에 따라 분리되도록 설정
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)


#최소 최대 정규화! x_train 을 기준값으로 삼고!! x값만 변환하기!

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
scaler.fit(X_train)
X_scaled_train =scaler.transform(X_train)
X_scaled_test= scaler.transform(X_test)


# 로지스틱회귀모델 적용

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_scaled_train,y_train) #정규화한 특성치 x값의 훈련데이터와 레이블 훈련데이터에 모델을 적용한다.
pred_train= model.predict(X_scaled_train) #예측치를 새로운 변수에 저장
model.score(X_scaled_train, y_train ) #정확도 확인

##훈련데이터 확인
# 오차행렬로 정분류와 오분류 확인

from sklearn.metrics import confusion_matrix

confusion_train = confusion_matrix(y_train,pred_train)
print('훈련데이터 오차행렬:\n', confusion_train)


#정밀도와 재현율 확인
from sklearn.metrics import classification_report
cfreport_train = classification_report(y_train, pred_train)
print(' 분류예측 리포트:\n', cfreport_train)


##테스트 데이터 확인

#테스트 데이터의 정확도 확인
pred_test =model.predict(X_scaled_test)
model.score(X_scaled_test,y_test)


#테스트 데이터의 오차행렬 정분류 오분류
confusion_test = confusion_matrix(y_test, pred_test)
print('테스트 데이터 오차행렬:\n',confusion_test)

#테스트 데이터의 정밀도 재현율
cfreport_test= classification_report(y_test, pred_test)
print('분류예측 레포트:\n', cfreport_test)


####하이퍼파라미터 C 값을 조정

#Grid Search 그리드 탐색
param_grid ={'C':[0.001, 0.01, 0.1,1,10,100]}

from sklearn.model_selection import GridSearchCV

grid_search= GridSearchCV(LogisticRegression(),param_grid, cv= 5)
grid_search.fit(X_scaled_train,y_train)

print (grid_search.best_params_)
print(grid_search.best_score_)


#랜덤서치
#하이퍼파라미터의 범위를 지정하고 그 안에서 무작위로 뽑아 수행

from scipy.stats import randint
param_distribs = {'C':randint(low=0.01, high=100)}# 최저와 최고 사이 범위 지정

from sklearn.model_selection import RandomizedSearchCV
random_search=RandomizedSearchCV(LogisticRegression(), param_distributions= param_distribs, n_iter=100 ,cv=5) #범위 사이 100번 무작위 추출
random_search.fit(X_scaled_train,y_train)


print (random_search.best_params_)
print(random_search.best_score_)


