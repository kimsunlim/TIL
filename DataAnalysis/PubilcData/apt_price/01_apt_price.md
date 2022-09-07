## 1 전국 신규 민간 아파트 분양가격 동향

2013년부터  최근까지 부동산 가격 변동 추세가 아파트 분양가에 반영될까?

### 1.1 다루는 내용
- 공공데이터를 활용해 전혀 다른 두개의 데이터를 가져와서 전처리하고 병합하기
- 수치형과 범주형 데이터 시각화 
- 


### 1.2 실습데이터 가져오기 


```python
%ls data_apt
```

     C 드라이브의 볼륨에는 이름이 없습니다.
     볼륨 일련 번호: 866A-7EEA
    
     C:\Users\김선림\data_apt 디렉터리
    
    2022-09-07  오전 12:42    <DIR>          .
    2022-09-07  오전 12:42    <DIR>          ..
    2022-09-07  오전 12:42    <DIR>          상가상권정보
    2022-09-07  오전 12:42    <DIR>          전국도시공원표준데이터
    2022-09-07  오전 12:42    <DIR>          전국신규민간아파트분양가격동향
                   0개 파일                   0 바이트
                   5개 디렉터리  451,154,673,664 바이트 남음



```python
#라이브러리 불러오기 
import pandas as pd
```









### 1.3 데이터셋

#### 1.3.1 전국 평균 분양가격(2013년9월~2015년 8월)

#### 1.3.2 주택도시보증공사_전국 평균 분양가격(2019년12월)







### 1.4 데이터 로드 

#### 1.4.1 최근파일로드


```python
#최근 분양가 파일 로드 
#주택도시보증공사
df_last=pd.read_csv("data_apt/전국신규민간아파트분양가격동향/주택도시보증공사_전국 평균 분양가격(2019년 12월).csv",encoding='cp949')
#인코딩 하는거 별표
df_last.shape
```


    (4335, 5)


```python
# head로 미리보기
df_last.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>5841</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>전용면적 60㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5652</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5882</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5721</td>
    </tr>
    <tr>
      <th>4</th>
      <td>서울</td>
      <td>전용면적 102㎡초과</td>
      <td>2015</td>
      <td>10</td>
      <td>5879</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 뒷부분 미리보기
df_last.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4330</th>
      <td>제주</td>
      <td>전체</td>
      <td>2019</td>
      <td>12</td>
      <td>3882</td>
    </tr>
    <tr>
      <th>4331</th>
      <td>제주</td>
      <td>전용면적 60㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4332</th>
      <td>제주</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>3898</td>
    </tr>
    <tr>
      <th>4333</th>
      <td>제주</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4334</th>
      <td>제주</td>
      <td>전용면적 102㎡초과</td>
      <td>2019</td>
      <td>12</td>
      <td>3601</td>
    </tr>
  </tbody>
</table>
</div>







#### 1.4.2 2015년 부터 최근까지 데이터 로드 


```python
#전국평균분양가격 로드
df_first=pd.read_csv("data_apt/전국신규민간아파트분양가격동향/전국 평균 분양가격(2013년 9월부터 2015년 8월까지).csv",encoding='cp949')
df_first.shape
```




    (17, 22)




```python
df_first.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2013년12월</th>
      <th>2014년1월</th>
      <th>2014년2월</th>
      <th>2014년3월</th>
      <th>2014년4월</th>
      <th>2014년5월</th>
      <th>2014년6월</th>
      <th>2014년7월</th>
      <th>2014년8월</th>
      <th>...</th>
      <th>2014년11월</th>
      <th>2014년12월</th>
      <th>2015년1월</th>
      <th>2015년2월</th>
      <th>2015년3월</th>
      <th>2015년4월</th>
      <th>2015년5월</th>
      <th>2015년6월</th>
      <th>2015년7월</th>
      <th>2015년8월</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>18189</td>
      <td>17925</td>
      <td>17925</td>
      <td>18016</td>
      <td>18098</td>
      <td>19446</td>
      <td>18867</td>
      <td>18742</td>
      <td>19274</td>
      <td>...</td>
      <td>20242</td>
      <td>20269</td>
      <td>20670</td>
      <td>20670</td>
      <td>19415</td>
      <td>18842</td>
      <td>18367</td>
      <td>18374</td>
      <td>18152</td>
      <td>18443</td>
    </tr>
    <tr>
      <th>1</th>
      <td>부산</td>
      <td>8111</td>
      <td>8111</td>
      <td>9078</td>
      <td>8965</td>
      <td>9402</td>
      <td>9501</td>
      <td>9453</td>
      <td>9457</td>
      <td>9411</td>
      <td>...</td>
      <td>9208</td>
      <td>9208</td>
      <td>9204</td>
      <td>9235</td>
      <td>9279</td>
      <td>9327</td>
      <td>9345</td>
      <td>9515</td>
      <td>9559</td>
      <td>9581</td>
    </tr>
    <tr>
      <th>2</th>
      <td>대구</td>
      <td>8080</td>
      <td>8080</td>
      <td>8077</td>
      <td>8101</td>
      <td>8267</td>
      <td>8274</td>
      <td>8360</td>
      <td>8360</td>
      <td>8370</td>
      <td>...</td>
      <td>8439</td>
      <td>8253</td>
      <td>8327</td>
      <td>8416</td>
      <td>8441</td>
      <td>8446</td>
      <td>8568</td>
      <td>8542</td>
      <td>8542</td>
      <td>8795</td>
    </tr>
    <tr>
      <th>3</th>
      <td>인천</td>
      <td>10204</td>
      <td>10204</td>
      <td>10408</td>
      <td>10408</td>
      <td>10000</td>
      <td>9844</td>
      <td>10058</td>
      <td>9974</td>
      <td>9973</td>
      <td>...</td>
      <td>10020</td>
      <td>10020</td>
      <td>10017</td>
      <td>9876</td>
      <td>9876</td>
      <td>9938</td>
      <td>10551</td>
      <td>10443</td>
      <td>10443</td>
      <td>10449</td>
    </tr>
    <tr>
      <th>4</th>
      <td>광주</td>
      <td>6098</td>
      <td>7326</td>
      <td>7611</td>
      <td>7346</td>
      <td>7346</td>
      <td>7523</td>
      <td>7659</td>
      <td>7612</td>
      <td>7622</td>
      <td>...</td>
      <td>7752</td>
      <td>7748</td>
      <td>7752</td>
      <td>7756</td>
      <td>7861</td>
      <td>7914</td>
      <td>7877</td>
      <td>7881</td>
      <td>8089</td>
      <td>8231</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>







#### 1.4.3 데이터 요약하기


```python
df_last.info()
#4335개의 엔트리,5개 컬럼
#분양가격은 4058임 이것은 결측치때문에 적게나옴
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4335 entries, 0 to 4334
    Data columns (total 5 columns):
     #   Column   Non-Null Count  Dtype 
    ---  ------   --------------  ----- 
     0   지역명      4335 non-null   object
     1   규모구분     4335 non-null   object
     2   연도       4335 non-null   int64 
     3   월        4335 non-null   int64 
     4   분양가격(㎡)  4058 non-null   object
    dtypes: int64(2), object(3)
    memory usage: 169.5+ KB









#### 1.4.4 결측치 보기 

isnull혹은 isna로 결측치를 확인 할수 있다



```python
#isnull로 결측치 구하기 
df_last.isnull().sum()
#True, False로 나옴 
```


    지역명          0
    규모구분         0
    연도           0
    월            0
    분양가격(㎡)    277
    dtype: int64




```python
#isna로 결측치 구하기
df_last.isna().sum()
```


    지역명          0
    규모구분         0
    연도           0
    월            0
    분양가격(㎡)    277
    dtype: int64





#### 1.4.5 데이터 타입 변경 

분양가격이 문자 타입으로 되어있는데 이것은 계산할수 없기에 수치데이터로 타입을 변환해야한다. 


```python
df_last['분양가격(㎡)']
#숫자인데 오브젝트 형태임 그래서 수치데이터로 변환하기 
#astype은 공백이 있어서 에러가 생김 
```




    0       5841
    1       5652
    2       5882
    3       5721
    4       5879
            ... 
    4330    3882
    4331     NaN
    4332    3898
    4333     NaN
    4334    3601
    Name: 분양가격(㎡), Length: 4335, dtype: object




```python
# 데이터 타입 변환한것을 새로운 컬럼을 생성해서 넣어주기
df_last["분양가격"]=pd.to_numeric(df_last['분양가격(㎡)'],errors='coerce')
df_last['분양가격']
#float형태
```




    0       5841.0
    1       5652.0
    2       5882.0
    3       5721.0
    4       5879.0
             ...  
    4330    3882.0
    4331       NaN
    4332    3898.0
    4333       NaN
    4334    3601.0
    Name: 분양가격, Length: 4335, dtype: float64





#### 1.4.6 평당분양가격 구하기 

분양가격을 평당 분양가격 기준으로 보기위해 3.3을 곱해서 '평당분양가격' 컬럼 만들기


```python
df_last['평당분양가격']=df_last['분양가격']*3.3
df_last
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역명</th>
      <th>규모구분</th>
      <th>연도</th>
      <th>월</th>
      <th>분양가격(㎡)</th>
      <th>분양가격</th>
      <th>평당분양가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>서울</td>
      <td>전체</td>
      <td>2015</td>
      <td>10</td>
      <td>5841</td>
      <td>5841.0</td>
      <td>19275.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>서울</td>
      <td>전용면적 60㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5652</td>
      <td>5652.0</td>
      <td>18651.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>서울</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5882</td>
      <td>5882.0</td>
      <td>19410.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>서울</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2015</td>
      <td>10</td>
      <td>5721</td>
      <td>5721.0</td>
      <td>18879.3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>서울</td>
      <td>전용면적 102㎡초과</td>
      <td>2015</td>
      <td>10</td>
      <td>5879</td>
      <td>5879.0</td>
      <td>19400.7</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4330</th>
      <td>제주</td>
      <td>전체</td>
      <td>2019</td>
      <td>12</td>
      <td>3882</td>
      <td>3882.0</td>
      <td>12810.6</td>
    </tr>
    <tr>
      <th>4331</th>
      <td>제주</td>
      <td>전용면적 60㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4332</th>
      <td>제주</td>
      <td>전용면적 60㎡초과 85㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>3898</td>
      <td>3898.0</td>
      <td>12863.4</td>
    </tr>
    <tr>
      <th>4333</th>
      <td>제주</td>
      <td>전용면적 85㎡초과 102㎡이하</td>
      <td>2019</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4334</th>
      <td>제주</td>
      <td>전용면적 102㎡초과</td>
      <td>2019</td>
      <td>12</td>
      <td>3601</td>
      <td>3601.0</td>
      <td>11883.3</td>
    </tr>
  </tbody>
</table>
<p>4335 rows × 7 columns</p>
</div>







#### 1.4.7 분양가격 요약하기 


```python
df_last.info()
#바뀐 타입과 새로운 컬럼 확ㅇ인 가능
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4335 entries, 0 to 4334
    Data columns (total 7 columns):
     #   Column   Non-Null Count  Dtype  
    ---  ------   --------------  -----  
     0   지역명      4335 non-null   object 
     1   규모구분     4335 non-null   object 
     2   연도       4335 non-null   int64  
     3   월        4335 non-null   int64  
     4   분양가격(㎡)  4058 non-null   object 
     5   분양가격     3957 non-null   float64
     6   평당분양가격   3957 non-null   float64
    dtypes: float64(2), int64(2), object(3)
    memory usage: 237.2+ KB



```python
# 변경전 컬럼인 분양가격 (m)컬럼 요약 /기술통계값 보기 
df_last['분양가격(㎡)'].describe()
```




    count     4058
    unique    1753
    top       2221
    freq        17
    Name: 분양가격(㎡), dtype: object




```python
#분양가격 컬럼 요약 
df_last['분양가격'].describe()
```




    count     3957.000000
    mean      3238.128633
    std       1264.309933
    min       1868.000000
    25%       2441.000000
    50%       2874.000000
    75%       3561.000000
    max      12728.000000
    Name: 분양가격, dtype: float64











#### 1.4.8 v규모구분을 전용면적 컬럼으로 변경

규모규분 컬럼은 전용면적에 대한 내용이있다. 그래서 전용면적이라는 컬럼을 새로 만들어주고 기존 규모구분 값에서 문구를 빼고 간결하게 만들어주기


```python
df_last['규모구분'].unique()
```




    array(['전체', '전용면적 60㎡이하', '전용면적 60㎡초과 85㎡이하', '전용면적 85㎡초과 102㎡이하',
           '전용면적 102㎡초과'], dtype=object)




```python
df_last['전용면적']=df_last['규모구분'].str.replace('전용면적','')
df_last['전용면적']=df_last['전용면적'].str.replace('초과','~')
df_last['전용면적']=df_last['전용면적'].str.replace('이하','')
df_last['전용면적']=df_last['전용면적'].str.replace(' ','').str.strip() #앞뒤의 공백까지 제거 

df_last['전용면적']
```




    0             전체
    1            60㎡
    2        60㎡~85㎡
    3       85㎡~102㎡
    4          102㎡~
              ...   
    4330          전체
    4331         60㎡
    4332     60㎡~85㎡
    4333    85㎡~102㎡
    4334       102㎡~
    Name: 전용면적, Length: 4335, dtype: object







#### 1.4.9 필요없는 컬럼제거하기


```python
#규모구분 drop
df_last=df_last.drop(['규모구분','분양가격(㎡)'],axis=1) #axis행 지정
```


```python
df_last.info()
#전처리 했더니 메모리 사용량 줄어듬 (효율적)
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4335 entries, 0 to 4334
    Data columns (total 6 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   지역명     4335 non-null   object 
     1   연도      4335 non-null   int64  
     2   월       4335 non-null   int64  
     3   분양가격    3957 non-null   float64
     4   평당분양가격  3957 non-null   float64
     5   전용면적    4335 non-null   object 
    dtypes: float64(2), int64(2), object(2)
    memory usage: 203.3+ KB















### 1.5 groupby로 데이터 집계


```python
#groupby는 시리즈 형태로 나옴
#지역명별 평균
df_last.groupby(['지역명']).mean()
#지역명별 평당 분양가격만 평균
df_last.groupby(['지역명'])['평당분양가격'].mean()

```




    지역명
    강원     7890.750000
    경기    13356.895200
    경남     9268.778138
    경북     8376.536515
    광주     9951.535821
    대구    11980.895455
    대전    10253.333333
    부산    12087.121200
    서울    23599.976400
    세종     9796.516456
    울산    10014.902013
    인천    11915.320732
    전남     7565.316532
    전북     7724.235484
    제주    11241.276712
    충남     8233.651883
    충북     7634.655600
    Name: 평당분양가격, dtype: float64




```python
#전용면적으로 분양가격 평균 구하기
df_last.groupby(['전용면적'])['평당분양가격'].mean()
```




    전용면적
    102㎡~       11517.705634
    60㎡         10375.137421
    60㎡~85㎡     10271.040071
    85㎡~102㎡    11097.599573
    전체          10276.086207
    Name: 평당분양가격, dtype: float64




```python
#지역명, 전용면적으로 평당분양가격 평균구하기(두개 그룹화)
df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack().round()
#unstack() 은 두번째 인덱스가 컬럼값으로 지정
#round()소수점 지우기
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>전용면적</th>
      <th>102㎡~</th>
      <th>60㎡</th>
      <th>60㎡~85㎡</th>
      <th>85㎡~102㎡</th>
      <th>전체</th>
    </tr>
    <tr>
      <th>지역명</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강원</th>
      <td>8311.0</td>
      <td>7567.0</td>
      <td>7486.0</td>
      <td>8750.0</td>
      <td>7478.0</td>
    </tr>
    <tr>
      <th>경기</th>
      <td>14772.0</td>
      <td>13252.0</td>
      <td>12524.0</td>
      <td>13678.0</td>
      <td>12560.0</td>
    </tr>
    <tr>
      <th>경남</th>
      <td>10358.0</td>
      <td>8689.0</td>
      <td>8619.0</td>
      <td>10018.0</td>
      <td>8659.0</td>
    </tr>
    <tr>
      <th>경북</th>
      <td>9157.0</td>
      <td>7883.0</td>
      <td>8061.0</td>
      <td>8774.0</td>
      <td>8079.0</td>
    </tr>
    <tr>
      <th>광주</th>
      <td>11042.0</td>
      <td>9431.0</td>
      <td>9911.0</td>
      <td>9296.0</td>
      <td>9904.0</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>13087.0</td>
      <td>11992.0</td>
      <td>11779.0</td>
      <td>11141.0</td>
      <td>11771.0</td>
    </tr>
    <tr>
      <th>대전</th>
      <td>14877.0</td>
      <td>9176.0</td>
      <td>9711.0</td>
      <td>9037.0</td>
      <td>9786.0</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>13208.0</td>
      <td>11354.0</td>
      <td>11865.0</td>
      <td>12073.0</td>
      <td>11936.0</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>23446.0</td>
      <td>23213.0</td>
      <td>22787.0</td>
      <td>25944.0</td>
      <td>22610.0</td>
    </tr>
    <tr>
      <th>세종</th>
      <td>10107.0</td>
      <td>9324.0</td>
      <td>9775.0</td>
      <td>9848.0</td>
      <td>9805.0</td>
    </tr>
    <tr>
      <th>울산</th>
      <td>9974.0</td>
      <td>9202.0</td>
      <td>10503.0</td>
      <td>8861.0</td>
      <td>10493.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>14362.0</td>
      <td>11241.0</td>
      <td>11384.0</td>
      <td>11528.0</td>
      <td>11257.0</td>
    </tr>
    <tr>
      <th>전남</th>
      <td>8168.0</td>
      <td>7210.0</td>
      <td>7269.0</td>
      <td>7909.0</td>
      <td>7284.0</td>
    </tr>
    <tr>
      <th>전북</th>
      <td>8194.0</td>
      <td>7610.0</td>
      <td>7271.0</td>
      <td>8276.0</td>
      <td>7293.0</td>
    </tr>
    <tr>
      <th>제주</th>
      <td>10523.0</td>
      <td>14022.0</td>
      <td>10621.0</td>
      <td>10709.0</td>
      <td>10785.0</td>
    </tr>
    <tr>
      <th>충남</th>
      <td>8689.0</td>
      <td>7911.0</td>
      <td>7819.0</td>
      <td>9120.0</td>
      <td>7815.0</td>
    </tr>
    <tr>
      <th>충북</th>
      <td>8195.0</td>
      <td>7103.0</td>
      <td>7264.0</td>
      <td>8391.0</td>
      <td>7219.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#연도 , 지역명으로 평당 분양가격 평균구하기
g=df_last.groupby(['연도','지역명'])['평당분양가격'].mean().unstack()
g
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>지역명</th>
      <th>강원</th>
      <th>경기</th>
      <th>경남</th>
      <th>경북</th>
      <th>광주</th>
      <th>대구</th>
      <th>대전</th>
      <th>부산</th>
      <th>서울</th>
      <th>세종</th>
      <th>울산</th>
      <th>인천</th>
      <th>전남</th>
      <th>전북</th>
      <th>제주</th>
      <th>충남</th>
      <th>충북</th>
    </tr>
    <tr>
      <th>연도</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>7188.060000</td>
      <td>11060.94</td>
      <td>8459.220000</td>
      <td>7464.160000</td>
      <td>7916.700000</td>
      <td>9018.900000</td>
      <td>8190.600000</td>
      <td>10377.400</td>
      <td>20315.680</td>
      <td>8765.020000</td>
      <td>9367.600000</td>
      <td>10976.020000</td>
      <td>6798.880000</td>
      <td>7110.400000</td>
      <td>7951.075000</td>
      <td>7689.880000</td>
      <td>6828.800</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7162.903846</td>
      <td>11684.97</td>
      <td>8496.730000</td>
      <td>7753.405000</td>
      <td>9190.683333</td>
      <td>10282.030000</td>
      <td>8910.733333</td>
      <td>10743.535</td>
      <td>21753.435</td>
      <td>8857.805000</td>
      <td>9582.574138</td>
      <td>11099.055000</td>
      <td>6936.600000</td>
      <td>6906.625000</td>
      <td>9567.480000</td>
      <td>7958.225000</td>
      <td>7133.335</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>7273.560000</td>
      <td>12304.98</td>
      <td>8786.760000</td>
      <td>8280.800000</td>
      <td>9613.977551</td>
      <td>12206.700000</td>
      <td>9957.158491</td>
      <td>11560.680</td>
      <td>21831.060</td>
      <td>9132.505556</td>
      <td>10666.935714</td>
      <td>11640.600000</td>
      <td>7372.920000</td>
      <td>7398.973585</td>
      <td>12566.730000</td>
      <td>8198.422222</td>
      <td>7473.120</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>8219.255000</td>
      <td>14258.42</td>
      <td>9327.670000</td>
      <td>8680.776923</td>
      <td>9526.953333</td>
      <td>12139.252632</td>
      <td>10234.106667</td>
      <td>12889.965</td>
      <td>23202.245</td>
      <td>10340.463158</td>
      <td>10241.400000</td>
      <td>11881.532143</td>
      <td>7929.845000</td>
      <td>8174.595000</td>
      <td>11935.968000</td>
      <td>8201.820000</td>
      <td>8149.295</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>8934.475000</td>
      <td>15665.54</td>
      <td>10697.615789</td>
      <td>9050.250000</td>
      <td>12111.675000</td>
      <td>14081.650000</td>
      <td>12619.200000</td>
      <td>13537.865</td>
      <td>28286.830</td>
      <td>11299.394118</td>
      <td>10216.250000</td>
      <td>13249.775000</td>
      <td>8219.275862</td>
      <td>8532.260000</td>
      <td>11828.469231</td>
      <td>8748.840000</td>
      <td>7970.875</td>
    </tr>
  </tbody>
</table>
</div>















### 1.6 pivot table로 집계하기 

- 그룹화 했던것을 피봇테이블로 똑같이 해보깅


```python
pd.pivot_table(df_last, index=['지역명'],values=['평당분양가격'],aggfunc='sum')
#aggfunc 기본값은 평균
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>평당분양가격</th>
    </tr>
    <tr>
      <th>지역명</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강원</th>
      <td>1909561.5</td>
    </tr>
    <tr>
      <th>경기</th>
      <td>3339223.8</td>
    </tr>
    <tr>
      <th>경남</th>
      <td>2289388.2</td>
    </tr>
    <tr>
      <th>경북</th>
      <td>2018745.3</td>
    </tr>
    <tr>
      <th>광주</th>
      <td>2000258.7</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>2899376.7</td>
    </tr>
    <tr>
      <th>대전</th>
      <td>2030160.0</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>3021780.3</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>5899994.1</td>
    </tr>
    <tr>
      <th>세종</th>
      <td>2321774.4</td>
    </tr>
    <tr>
      <th>울산</th>
      <td>1492220.4</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>2931168.9</td>
    </tr>
    <tr>
      <th>전남</th>
      <td>1876198.5</td>
    </tr>
    <tr>
      <th>전북</th>
      <td>1915610.4</td>
    </tr>
    <tr>
      <th>제주</th>
      <td>2461839.6</td>
    </tr>
    <tr>
      <th>충남</th>
      <td>1967842.8</td>
    </tr>
    <tr>
      <th>충북</th>
      <td>1908663.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#전용면적으로 분양가격 평균 구하기

pd.pivot_table(df_last, index=['전용면적'],values=['평당분양가격'],aggfunc='mean')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>평당분양가격</th>
    </tr>
    <tr>
      <th>전용면적</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>102㎡~</th>
      <td>11517.705634</td>
    </tr>
    <tr>
      <th>60㎡</th>
      <td>10375.137421</td>
    </tr>
    <tr>
      <th>60㎡~85㎡</th>
      <td>10271.040071</td>
    </tr>
    <tr>
      <th>85㎡~102㎡</th>
      <td>11097.599573</td>
    </tr>
    <tr>
      <th>전체</th>
      <td>10276.086207</td>
    </tr>
  </tbody>
</table>
</div>




```python
#지역명, 전용면적으로 평당분양가격 평균구하기(두개 그룹화)
pd.pivot_table(df_last, index=['지역명'], columns=['전용면적'],values=['평당분양가격'],aggfunc='mean')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead tr th {
        text-align: left;
    }
    
    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="5" halign="left">평당분양가격</th>
    </tr>
    <tr>
      <th>전용면적</th>
      <th>102㎡~</th>
      <th>60㎡</th>
      <th>60㎡~85㎡</th>
      <th>85㎡~102㎡</th>
      <th>전체</th>
    </tr>
    <tr>
      <th>지역명</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강원</th>
      <td>8311.380000</td>
      <td>7567.098000</td>
      <td>7485.588000</td>
      <td>8749.557143</td>
      <td>7477.536000</td>
    </tr>
    <tr>
      <th>경기</th>
      <td>14771.790000</td>
      <td>13251.744000</td>
      <td>12523.566000</td>
      <td>13677.774000</td>
      <td>12559.602000</td>
    </tr>
    <tr>
      <th>경남</th>
      <td>10358.363265</td>
      <td>8689.175000</td>
      <td>8618.676000</td>
      <td>10017.612000</td>
      <td>8658.672000</td>
    </tr>
    <tr>
      <th>경북</th>
      <td>9157.302000</td>
      <td>7883.172000</td>
      <td>8061.372000</td>
      <td>8773.814634</td>
      <td>8078.532000</td>
    </tr>
    <tr>
      <th>광주</th>
      <td>11041.532432</td>
      <td>9430.666667</td>
      <td>9910.692000</td>
      <td>9296.100000</td>
      <td>9903.630000</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>13087.338000</td>
      <td>11992.068000</td>
      <td>11778.690000</td>
      <td>11140.642857</td>
      <td>11771.298000</td>
    </tr>
    <tr>
      <th>대전</th>
      <td>14876.871429</td>
      <td>9176.475000</td>
      <td>9711.372000</td>
      <td>9037.430769</td>
      <td>9786.018000</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>13208.250000</td>
      <td>11353.782000</td>
      <td>11864.820000</td>
      <td>12072.588000</td>
      <td>11936.166000</td>
    </tr>
    <tr>
      <th>서울</th>
      <td>23446.038000</td>
      <td>23212.794000</td>
      <td>22786.830000</td>
      <td>25943.874000</td>
      <td>22610.346000</td>
    </tr>
    <tr>
      <th>세종</th>
      <td>10106.976000</td>
      <td>9323.927027</td>
      <td>9775.458000</td>
      <td>9847.926000</td>
      <td>9805.422000</td>
    </tr>
    <tr>
      <th>울산</th>
      <td>9974.448000</td>
      <td>9202.106897</td>
      <td>10502.531707</td>
      <td>8861.007692</td>
      <td>10492.712195</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>14362.030435</td>
      <td>11241.318000</td>
      <td>11384.406000</td>
      <td>11527.560000</td>
      <td>11257.026000</td>
    </tr>
    <tr>
      <th>전남</th>
      <td>8168.490000</td>
      <td>7210.170000</td>
      <td>7269.240000</td>
      <td>7908.862500</td>
      <td>7283.562000</td>
    </tr>
    <tr>
      <th>전북</th>
      <td>8193.570000</td>
      <td>7609.932000</td>
      <td>7271.352000</td>
      <td>8275.781250</td>
      <td>7292.604000</td>
    </tr>
    <tr>
      <th>제주</th>
      <td>10522.787234</td>
      <td>14022.221053</td>
      <td>10621.314000</td>
      <td>10709.082353</td>
      <td>10784.994000</td>
    </tr>
    <tr>
      <th>충남</th>
      <td>8689.169388</td>
      <td>7911.156000</td>
      <td>7818.954000</td>
      <td>9120.045000</td>
      <td>7815.324000</td>
    </tr>
    <tr>
      <th>충북</th>
      <td>8195.352000</td>
      <td>7103.118000</td>
      <td>7264.488000</td>
      <td>8391.306000</td>
      <td>7219.014000</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
