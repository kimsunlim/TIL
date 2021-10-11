# visualization[02]



1.필요 import  :**매우 유용**

```python
import pandas as pd
import numpy  as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
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
    
    
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
```





- 데이터 빈도(히스토그램, 박스)
- 데이터 전처리
- 변수 검토
- 변수간 관계 분석 및 시각화



2. 엑셀 불러오기

```python
xls = pd.ExcelFile('./data/koweps_visualization.xlsx')
koweps_df = xls.parse(xls.sheet_names[0])

#데이터에 담기
data_df = koweps_df.copy()
data_df.head()

```



3. image import

```python
from IPython.display import Image
Image('c:/img/koweps_img.png', width = 700)
```



4. 해당 데이터 프레임에서 제공해 드린 컬럼들만 추출하여 사용하고자하는 컬럼들만 rename하세요

```python
want_columns_df = data_df[ ['h12_g3', 'h12_g4', 'h12_g10', 'h12_g11', 'h12_eco9', 'p1202_8aq1', 'h12_reg7'] ]
want_columns_df.columns = ['성별', '태어난 연도', '혼인상태', '종교', '직종', '일한달의 월 평균 임금', '7개 권역별 지역구분']
want_columns_df.head(10)

```



5. 데이터 분석

```python
#성별 추출

gender_filter_df = want_columns_df.filter(['성별'])
gender_filter_df.head()

#성별값을 남,여로 변경
gender_filter_df['성별2'] = np.where(gender_filter_df['성별'] == 1 , '남자' , '여자')
gender_filter_df.head()


# 결측값 확인
gender_filter_df.isna().sum()


# 데이터 분포 확인
gender_count = gender_filter_df['성별2'].value_counts()
gender_count

# 시리즈를 데이터 프레임으로 변환!!

gedner_count_df = pd.DataFrame(gender_count)
gedner_count_df.head()



gedner_count_df.rename(columns = {'성별2' : '명'} , inplace=True)
gedner_count_df

# 비율순으로 정렬
gedner_count_df.sort_values('명' , inplace=True)
gedner_count_df
```



6.성별 분포를 시각화

```python
# 성별 분포를 시각화 
gedner_count_df.plot.bar(rot=0)
plt.grid()
plt.title('성별 분포')
plt.xlabel('성별')
plt.ylabel('명')


for idx, value in enumerate(list( gedner_count_df['명'] )) :
    txt = '%d명' % value
    plt.text(idx, value, txt , 
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=14,
            color='red')

plt.show()


#chart


gender_count.plot.pie(autopct='%d%%', 
                          legend=True, 
                          shadow=True,
                          labels = gender_count.index)
plt.axis('equal')
plt.show()
```





------

#### 성별에 따른 평균 급여 차이 분석



1.

```python
#데이터 확인
want_columns_df.head()

#성별과 월급데이터만 추출
gender_salary_df = want_columns_df.filter(['성별', '일한달의 월 평균 임금'])
gender_salary_df.head()

# 성별을 남자와 여자로 변환
gender_salary_df['성별'] = np.where(gender_salary_df['성별'] == 1 , '남자' , '여자')
gender_salary_df.head()

# 데이터 정제(결측값 확인, 결측값 제거, 이상치 결측 처리)
print(gender_salary_df.isna().sum())
gender_salary_df.dropna(inplace = True)
print("*" * 50)
print(gender_salary_df.isna().sum())

# 이상치 결측 처리
# 급여 범위를 벗어나면 nan 대체하고 결측치 처리 ~
gender_salary_df['일한달의 월 평균 임금'] = np.where(
    ((gender_salary_df['일한달의 월 평균 임금'] < 1) | ( gender_salary_df['일한달의 월 평균 임금'] > 9998)) ,
    np.nan , gender_salary_df['일한달의 월 평균 임금'] )
gender_salary_df.head()

```



2.

```python
# 데이터 분석(성별로 그룹화하여 그룹별 평균)
gender_salary_mean_df = gender_salary_df.groupby('성별').mean()
gender_salary_mean_df.head()
```



3.시각화

```python
# 성별에 평균 급여 차이 분석 시각화
gender_salary_mean_df.plot.bar(rot=0)
plt.grid()
plt.title('성별에 평균 급여 차이 분석 시각화')
plt.xlabel('성별')
plt.ylabel('급여')


for idx, value in enumerate(list( gender_salary_mean_df['일한달의 월 평균 임금'] )) :
    txt = '%d만원' % value
    plt.text(idx, value, txt , 
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=10,
            color='red')

plt.show()
```





-------

#### 나이에 따른 평균 급여 변화

1.

```python
#데이터 추출
year_salary_df =want_columns_df.filter(['태어난 연도', '일한달의 월 평균 임금'])
year_salary_df.head()


# 나이를 계산하여 파생변수 추가
now_year = dt.datetime.now().year
# now_year
year_salary_df['나이'] = now_year - year_salary_df['태어난 연도'] + 1
year_salary_df.head()

# 데이터 정제(결측값 확인)
year_salary_df.isna().sum()



# 이상치 정제
# 코드표에서 제시한 범위를 벗어난 값(1보다 작거나 9998보다 큰 값)은 이상치 이므로 결측치로 변경해야 한다.

year_salary_df['일한달의 월 평균 임금'] = np.where(
    ((year_salary_df['일한달의 월 평균 임금'] < 1) | (year_salary_df['일한달의 월 평균 임금'] > 9998)), 
    np.nan, 
    year_salary_df['일한달의 월 평균 임금'])
year_salary_df.isna().sum()  # 결측치 확인

year_salary_df.dropna(inplace=True)
year_salary_df.isna().sum()
```

2. 데이터 분석

```python
# 데이터 분석

year_salary_df = year_salary_df.filter(['나이','일한달의 월 평균 임금']).groupby('나이').mean()
year_salary_df.head(
```



3.시각화

```python
# 시각화
year_salary_df.plot()
plt.rcParams['figure.figsize'] = (10,5)
plt.title('나이에 따른 평균 월급 변화')
plt.grid()
plt.xlabel('나이')
plt.ylabel('평균월급')
plt.show()
```





------

#### 연령대 분포 분석

1.데이터 추출

```python
year_df = want_columns_df.filter(['태어난 연도'])
year_df.head()


# 나이를 계산 파생변수 추가
year_df['나이'] = dt.datetime.now().year - year_df['태어난 연도'] + 1
year_df.head()


# 연령대를 분석하기 위한 파생변수 추가
year_df['연령대'] = ( year_df['나이'] // 10 ) * 10
year_df.head()

# 결측값 확인 절차 및 정제
year_df.isna().sum()
```



2. 빈도수 확인

   ```python
   # 연령대에 대한 빈도수 확인
   # age_gen_df = year_df.filter(['나이','연령대']).groupby('연령대').count()
   # age_gen_df
   
   # type( year_df['연령대'].value_counts() )
   # type( year_df.filter(['연령대']).count() )
   
   age_gen_df2 = pd.DataFrame( year_df['연령대'].value_counts() )
   age_gen_df2.sort_index(inplace=True)
   age_gen_df2
   
   
   # 인덱스를 의미 있는 이름으로 수정
   reIndex = {}
   for idx in list(age_gen_df2.index) :
       reIndex[idx] = '%d대' % idx
   # reIndex
   age_gen_df2.rename(index=reIndex , inplace=True)
   age_gen_df2
   ```

   

3. 시각화

```python
# 시각화 bar()
age_gen_df2.plot.bar(rot=0)
plt.grid()
plt.title('연령대 분석 시각화')
plt.xlabel('연령대')
plt.ylabel('명')


for idx, value in enumerate(list( age_gen_df2['연령대'] )) :
    txt = '%d명' % value
    plt.text(idx, value, txt , 
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=10,
            color='red')

plt.show()
```

+

```python
# 시각화1.
gedner_gen_dist_pivot.plot.bar(rot=0)
plt.title('성별과 연령대별 분포')
plt.grid()
plt.xlabel('연령대')
plt.ylabel('명')

plt.show()


# 시각화2.
gedner_gen_dist_pivot.plot(rot=0)
plt.title('성별과 연령대별 분포')
plt.grid()
plt.xlabel('연령대')
plt.ylabel('명')

plt.show()
```

