
# 작업형1
#mtcars 데이터셋의 qsec컬럼을 최소최대 척도로 변환한후 0.5보다 쿤값을 가지는 레코드수는?


# 데이터 불러오기

import pandas as pd
df = pd.read_csv('data/mtcars.csv', index_col=0)

from sklearn.preprocessing import MinMaxScaler
scaler=['qsec']
min=MinMaxScaler()

min.fit(df[scaler])
df[scaler]=min.transform(df[scaler])

result=df[df[scaler]>0.5]  ##df로 한번 더 감싸는거 매우 명심!!!

print(len(result))



#작업형2

#소수점 확률보고 predict proba사용해야한다는 것 을 봐야함

# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
X_test = pd.read_csv("data/X_test.csv")
X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv")

# 사용자 코딩

##1. 결측치 제거
#0넣어주기
X_train['환불금액']=X_train['환불금액'].fillna(0)
X_test['환불금액']=X_test['환불금액'].fillna(0)

#print(X_train['환불금액'].isnull().sum())


#2.라벨인코딩
label=['주구매상품','주구매지점']
from sklearn.preprocessing import LabelEncoder

X_train[label]=X_train[label].apply(LabelEncoder().fit_transform)
X_test[label]=X_test[label].apply(LabelEncoder().fit_transform)


#print(X_train['주구매지점'].head())

#3.데이터변환, 더미처리
#print(X_train['주구매상품'].value_counts())
#print(X_train['주구매지점'].value_counts())

category=['주구매지점']

for i in category:
	X_train[i]=X_train[i].astype('category')
	X_test[i]=X_test[i].astype('category')

X_train=pd.get_dummies(X_train)
X_test=pd.get_dummies(X_test)


#print(X_train.head())


#4.파생변수
#연속적인값 !!> 총구매액
X_train['총구매액_qcut']= pd.qcut(X_train['총구매액'],5, labels=False)
X_test['총구매액_qcut']= pd.qcut(X_test['총구매액'],5, labels=False)

#print(X_train.head())

#5. 스케일링

from sklearn.preprocessing import MinMaxScaler
scaler=['총구매액','최대구매액','환불금액','내점일수','내점당구매건수','주말방문비율','구매주기']
min=MinMaxScaler()
min.fit(X_train[scaler])
X_train[scaler]=min.transform(X_train[scaler])
X_test[scaler]=min.transform(X_test[scaler])
#print(X_train.head())


#6.데이터셋 분리

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid=train_test_split(X_train, y_train['gender'],test_size=0.2, random_state=42, stratify= y_train['gender'])

#print(X_train.shape)
#print(X_valid.shape)


#7. 모형학습
#1)로지스틱
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression()
model1.fit(X_train,y_train)
pred1=pd.DataFrame(model1.predict_proba(X_valid))


#2)랜포


from sklearn.ensemble import RandomForestClassifier
model2=RandomForestClassifier()
model2.fit(X_train,y_train)
pred2= pd.DataFrame(model2.predict_proba(X_valid))

#8. 앙상블 모델학습

#앙상블 보팅
from sklearn.ensemble import VotingClassifier
model3=VotingClassifier(estimators=[('logistic',model1),('rf',model2)], voting='soft')
model3.fit(X_train,y_train)
pred3=pd.DataFrame(model3.predict_proba(X_valid))


#9. 모형 평가
from sklearn.metrics import roc_auc_score
print('로지 정확도', roc_auc_score(y_valid, pred1.iloc[:,1]))#첫번째열만 가져와서 비교
print('랜포 정확도', roc_auc_score(y_valid, pred2.iloc[:,1]))
print('보팅 정확도', roc_auc_score(y_valid, pred3.iloc[:,1]))

##보팅이 젤 높음

#10. 하이퍼 파라미터 튜닝
from sklearn.model_selection import GridSearchCV
parameters={'n_estimators':[50,100], 'max_depth':[4,6]}
madel4=RandomForestClassifier()
dlf=GridSearchCV(estimator=madel4,param_grid=parameters, cv=3)
dlf.fit(X_train,y_train)

print('최적의 파라미터', dlf.best_params_)

#11. 데이터 저장

result=pd.DataFrame(model3.predict_proba(X_test))
#아까는 검증용으로 테스트를함 이제는 실제 test데이터로 학습해서 예측 적용

result=result.iloc[:,1]#1번째열 인덱스 제거 >>밑에서 cust_id넣어야함
pd.DataFrame({'cust_id':X_test['cust_id'],'gender':result}).to_csv('0010.csv',index=False)

#확인작업
check=pd.read_csv('0010.csv')
print(check.head())


# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)
