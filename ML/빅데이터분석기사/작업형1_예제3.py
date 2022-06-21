
#작업형 1_예제3

##1번
#주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을
#구하고, 그 차이를 구해보라
# 소수첫째자리까지 출력


# 메보
#1.국가별로 접종데이터가 있으므로 그룹화후 맥스값 설정 (시간에 따라 접종률 올라가서)
#2.접종률 정렬 
#3.top상위 10개국
#4.bottom 하위 10개국
#5. 두변수 뺀후 반올림 한자리


import pandas as pd 
df=pd.read_csv('"../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv"')


#1.국가별로 접종데이터가 있으므로 그룹화후 맥스값 설정 (시간에 따라 접종률 올라가서)
df2= df.groupby('country').max()


#이상치 제거 
df2=df[1:]

#2.접종률 정렬 
df2= df2.sort_values(by='ratio', ascending=False)

#3.top상위 10개국
top=df2['ratio'].head(10).mean()

#4.bottom 하위 10개국
bottom=df2['ratio'].tail(10).mean()


#5. 두변수 뺀후 반올림 한자리
print(round(top-bottom),1)




##2번
## 상관관계 구하기
# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력



#1. 상관관계구하기
#2. quality 상관관계 가장 큰 max.min값 추출
#3. 구한값 더하기
#4.상관관계에서 quality 제외, 소수점 둘째자리 round



import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv("../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv")
#print(df.head())



#1. 상관관계구하기
df_corr=df.corr()
#print(df_corr)

# quality-quality의 상관관계제거 
df_corr=df_corr[:-1] #맨 뒷
print(df_corr['quality'])


#2. quality 상관관계 가장 큰 max.min값 추출

max= df_corr['quality'][:-1].max()
min=df_corr['quality'][:-1].min()



#3. 구한값 더하기
print(round(max+min),2)





##3번 
#2022년 데이터중 2022년 중앙값보다 큰 값의 데이터 수 


import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data2.csv", index_col='year')
df

##year 년도가 중심이니깐 index_col인 인덱스 컬럼 지정해주기!!

a= df.loc['2022년'].median()
print(sum(df.loc['2022년',:]>a))


##iloc는 행과 컬럼 추출  > df.iloc[행, 열]  >>행과 열 번째 값들만 추출해줘
#ioc는 행이름 df.loc[행] >> 인덱스 이름이 행인 행만 추출해줘,, 인덱스 라벨값!






##4번 
#결측치 데이터 행을 제거하고 앞에서부터 60%데이터만 활용해, f1컬럼 3사분위값을 구해라


#1. 결측치 행 제거 
#2. 60%데이터만 추출 
#3.f1칼럼의 3 사분위수 


import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
df


df=df.dropna()
df=df.iloc[:int(len(df)*0.6)]

print(df['f1'].quantile(0.75))




##5번
#결측치가 제일 큰 값의 컬럼명르 구하시오 


import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
df.head()

#1. 결측치 확인 

df.isnull().sum()

#결측치가 젤큰값 컬럼명 
print(df.index[3])  ##index쓰면 컬럼 명 추출! 



