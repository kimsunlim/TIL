# visualization[01]

- 시각화 패키지 matplotlib
- 서브 패키지 pyplot
- seaborn
- 분석된 내용을 시각화
- Pandas 시각화 기능







\<import>

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
%matplotlib inline


# 한글 폰트 문제 해결
import platform

from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 
```



- line plot :데이터가 시간, 순서 등에 따라 어떻게 변화 하는지 보여줌



```python
plt.title('line plot')    #제목
plt.plot([10,20,30,40],[1,4,9,16],'rs--')  #축, 데이터, 선스타일
plt.xlabel('x 라벨')
plt.ylabel('y 라벨')   #라벨이름

plt.show()
```

![vis01](./이미지/vis01.PNG)





- option(color,marker, style)
- color ->b(blue),g(green),r(red)
- marker ->,.
- line style -> --,..,:

```python
plt.title('스타일 적용 예시')
plt.plot([10,20,30,40],[1,4,9,16],
        c='b',
        lw=5,
        ls='--',marker='o',ms=15, mec='g',mew=5,mfc='r')
plt.xlabel('x 라벨')
plt.ylabel('y 라벨')
plt.xlim(0,50)
plt.ylim(-10,30)  #구간 설정
plt.show()
```

![line_style](C:\img\line_style.png)





- tick 축에 표시되는 하나의 지점(xticks,yticks)

```python
X= np.linspace(-np.pi,np.pi,256)
Y= np.cos(X)
plt.plot(X,Y)
plt.xticks([-np.pi,-np.pi/2,0 ,-np.pi/2,-np.pi])
plt.yticks([-1,0,+1])
plt.grid(True)  #격자무늬
plt.show()
```

![ㄴ](C:\Users\i\Desktop\ㄴ.PNG)

- 여러개 라인

```python
X=np.linspace(-np.pi,np.pi,256)
Y_C,Y_S=np.cos(X),np.sin(X)
plt.plot(X,Y_C,ls='--',label='cosine')
plt.plot(X,Y_S,ls='--',label='sine')
plt.legend(loc=0)
plt.show()

```

![-](C:\Users\i\Desktop\-.PNG)





- matplotlilb그림을 그리는 객체, Figure,Axes,Axis객체를 포함하고 있다.
- Figure -> 그림이 그려지는 종이 뜻
- Axes ->플롯
- Axis ->축



```python
np.random.seed(100)
plt.figure(figsize=(10,2))
plt.plot(np.random.randn(100))
plt.show()
```

![ㅕ](C:\Users\i\Desktop\ㅕ.PNG)

- subplot(2,1,1)
- subplot(2,1,2)





\<데이터생성>

```python
X1 =np.linspace(0.0,5.0)
Y1 = np.cos(2 * np.pi* X1) *np.exp(-X1)
print(X1)
print(Y1)

X2 =np.linspace(0.0,2.0)
Y2 = np.cos(2 * np.pi* X2) 
print(X2)
print(Y2)
```



```python
axes01=plt.subplot(2,1,1)
plt.plot(X1,Y1)
plt.title('subplot 01')

axes02=plt.subplot(2,1,2)
plt.plot(X2,Y2)
plt.title('subplot 02')

plt.tight_layout()#자동으로 간격을 맞춰주는 역할
plt.show()
```

![캡처ㄴ](C:\Users\i\Desktop\캡처ㄴ.PNG)





### 플롯의 유형

- line plot
- scatter plot
- contour plot
- surface plot
- bar plot
- histogram plot
- box plot





=barplot : x 데이터는 카테고리 값인 경우가 대부분

```python
Y=[2,3,1]
X=np.arange(len(Y))

xlabel=['1등실','2등실','3등실']
plt.title('bar plot')
plt.bar(X,Y)
plt.xticks(X,xlabel)
plt.yticks(sorted(Y))
plt.xlabel('선실등급')
plt.ylabel('생존자 수')
plt.show()
```

![ㄴㅊㅍ](C:\Users\i\Desktop\ㄴㅊㅍ.PNG)





1.종을 기준으로 그룹화 하여 각 그룹의 평균을 구해 봐



```python
specise_mean=iris.groupby(['Y']).mean()
specise_mean.T

# bar plot
specise_mean.T.plot.bar(rot=0)
plt.title('각 변수별 평균')
plt.xlabel('편균')
plt.ylabel('변수')
plt.ylim(0,8)

plt.show()
```

![쇼](C:\Users\i\Desktop\쇼.PNG)



```python
iris[['SL','Y']].boxplot(by='Y')
plt.title('종에 따른 SL 박스플롯임')
plt.xlabel('type')
plt.ylabel('cm')
plt.tight_layout(pad=3)   #간격
plt.show()

```

![ㅐ](C:\Users\i\Desktop\ㅐ.PNG)





- 4가지

```python
fig, axes=plt.subplots(nrows=2,ncols=2,figsize=(20,10))

ax=axes.flatten()



iris[['SL','Y']].boxplot(by='Y',ax=ax[0])
plt.title('종에 따른 SL 박스플롯임')
plt.xlabel('type')
plt.ylabel('cm')

iris[['SW','Y']].boxplot(by='Y',ax=ax[1])
plt.title('종에 따른 SW 박스플롯임')
plt.xlabel('type')
plt.ylabel('cm')

iris[['PL','Y']].boxplot(by='Y',ax=ax[2])
plt.title('종에 따른 PL 박스플롯임')
plt.xlabel('type')
plt.ylabel('cm')

iris[['PW','Y']].boxplot(by='Y',ax=ax[3])
plt.title('종에 따른 PW 박스플롯임')
plt.xlabel('type')
plt.ylabel('cm')

plt.show()
plt.show()
```

![3](C:\Users\i\Desktop\3.PNG)





## car_mpg.xls [실습



1.엑셀 파일 불러오기

```python
xls= pd.ExcelFile('./data/car_mpg.xlsx')

data_df=xls.parse(xls.sheet_names[0])
data_df.head()

data_df.info() #데이터 정보를 확인해주기!!

row,col =data_df.shape
print('row : ',row)
print('col : ',col)

data_df.describe()  #기술 통계값 확인!
```





- 양적자료: 요약정보에 집계가 되는 컬럼으로 관측된 값이 수치 형태의 속성을 가지는 자료
- 양적자료의 시각화 : boxplot
- 배기량,생산년도,실린더 개수, 도시연비,고속도로연비

- 질적 자료: 범주 또는 순서 형태의 속성을 가지는 자료로서 도수 분포표와 히스토그램으로 데이터의 분포를 확인해야하는 값들
- 제조회사, 모델명, 변속기 종류, 구동방식, 연료 종류, 자동차종류





```python
data_df.boxplot(['displ','cyl','cty','hwy']) #양적자료의 데이터 분포 확인(boxplot)
plt.show()
```

![ㅊ](C:\Users\i\Desktop\ㅊ.PNG)







```python
# 질적 자료에 대한 데이터 빈도 확인
# 제조회사, 모델명, 변속기 종류, 구동방식, 연료 종류, 자동차 종류

data_df['manufacturer'].value_counts()
data_df['model']



data_df['model'].value_counts()  #value_counts()로 데이터 확인가능
```



1.자동차 배기량에(displ) 따라 고속도로 연비가(hwy) 다른지를 알아보자^*^
=배기량이 4이하인 자동차와 5이상인 자동차 중 어떤 자동차의 고속도로 연비가 평균적으로 
=높은지를 알아보자



```python
data_df.query('displ <=4')['hwy'].mean()
data_df.query('displ >=5')['hwy'].mean()

query_df =pd.DataFrame(np.random.randint(0,10, size=(10,3)), columns=['col01','col02','col03'])
query_df
```

 

2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
   audi와 toyota중 어느 manufacturer(자동차 제조회사)의 cty(도시연비)가 평균적으로 더 높은지 알아보시오



```python
print(data_df[data_df['manufacturer']=='audi']['cty'].mean())
print(data_df[data_df['manufacturer']=='toyota']['cty'].mean())
print(data_df.query('manufacturer== "audi"')['cty'].mean())
print(data_df.query('manufacturer== "toyota"')['cty'].mean())
```





3.chevrolet,ford,honda 자동차의 고속도로 연비 평균을 알아보려고 한다. 

 이회사들의 데이터를 추출한 후 hwy전체 평균을 확인하시오.

```python
maufac_car=['chevrolet','ford','honda']
print(data_df.query('manufacturer in @maufac_car')['hwy'].mean())

print (data_df.query('manufacturer == "chevrolet" or \
                      manufacturer == "ford" or \
                      manufacturer == "honda"') ['hwy'].mean())
                     
                   

print(data_df[(data_df['manufacturer']=='chervrolet') |
              (data_df['manufacturer']=='ford') |
              (data_df['manufacturer']=='honda')]['hwy'].mean())


#####같은거

chevrolet_index =data_df['manufacturer'] == 'chevrolet'
ford_index =data_df['manufacturer'] == 'ford'
honda_index =data_df['manufacturer'] == 'honda'

temp_df =data_df.loc[chevrolet_index | ford_index | honda_index, :]
mean_df= temp_df[['manufacturer','hwy']].groupby(temp_df.manufacturer).agg(np.mean)
mean_df.plot.bar()

display(mean_df)
print('세 자동차 회사의 hwy의 평균 :',temp_df['hwy'].mean())

```

![8](C:\Users\i\Desktop\8.PNG)



4. 데이터 병합

```python
#데이터
fl_df=pd.DataFrame({
    'fl':['c','d','e','p','r'],
    'price_fl':[2.35,2.38,2.11,2.76,2.22]
})
fl_df

#우리가 만든 연료 가격 프레임을 원본 프레임에 병합

data_fl_merge_df =pd.merge(data_df,fl_df, on='fl',how='inner')
data_fl_merge_df.head()

#머지한 데이터 프레임에서 model,fl, price_fl만 추출

data_fl_merge_df.filter(['model','fl','price_fl']).head()

#데이터 전처리 과정에서 결측값 확인하기

data_fl_merge_df.isna().sum()
```





```python
#구동 방식(dry)별 고속도로 연비(hwy)평균
#임의적으로 결측값 처리를 위해서 더미 값을 넣어 보도록 하자

data_fl_merge_df.loc[65,'hwy']=np.nan
data_fl_merge_df.loc[120,'hwy']=np.nan
data_fl_merge_df.loc[154,'hwy']=np.nan
data_fl_merge_df.loc[189,'hwy']=np.nan
data_fl_merge_df.loc[219,'hwy']=np.nan
data_fl_merge_df.loc[230,'hwy']=np.nan


data_fl_merge_df.filter(['drv','hwy']).isna().sum()
data_fl_merge_df['drv'].value_counts()
```



```python
#hwy 변수의 결측값을 제외하고 어떤 구동방식의 고속도로 평균 연비가 높은지 알아보자


data_fl_merge_isna_df=data_fl_merge_df.filter(['drv','hwy']).dropna()
print(data_fl_merge_df.info())

data_fl_merge_isna_df.groupby('drv').mean()
```



```python
# 구동방식별 연비평균을 비교하기 위한 막대그래프로 시각화 해보자

a_df=data_fl_merge_isna_df.groupby('drv')['hwy'].mean()
a_df.plot.bar(rot=0)

plt.title('구동방식별 평균연비')

plt.xlabel('구동방식')
plt.ylabel('연비')

plt.grid()
plt.show()
```

