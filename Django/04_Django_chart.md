## 4. Django



>  **mvc**                 **mvt**

model(db)         model (db)

view(html)         view(views)

c(view)                t (html)



> **1.csv -> model**
>
> **2.django - 파일 업로드(.csv)**
>
> **3.visualization(시각화)- script(json)**
>
> **4.numpy - pandas**
>
> **5.script - jquery, d3, goole chart, highchart**
>
> **6. ajax -jquery **



**비정형 데이터 - dataframe(pandas)   -  (.csv)   -  model(class)**

엑셀 ->DB : 위의 경로를 모를경우, python code DB연동 해야함



## 1) 차트

1. App생성 : python manage.py chartApp

​    (**웹** settings에 생성한 chartApp등록, urls 에 path('chart/',  include('ChartApp.urls')) 등록!)



- figure:이미지와 텍스트 불러옴

```python
<figure class ="highcharts-figure">
        <div id="container"></div>
        <p>
        <center>
        차트는 가독성과 이해도를 높일 수 있습니다.
        <b> -Written By jslim </b>
        </center>
        </p>
    </figure>
```







- 옵션: **{key:value}**

1. chart 차트타입

2. title: 타이틀 이름

3. subtitle

4. xAxis :x축,  yAxis :y축













#### +chartApp에서 line chart, bar chart, wordcloud등 생성 가능

> **line chart**



1. chart_index.html 생성 하고**\<a href="../line"><li>  line chart </li></a>** 링크들을 걸어줘야 함
2. urls 등록 :path('line/',  views.line , name='line'

3. templates에 chart_line.html 생성 -> https://www.highcharts.com/demo 차트 형식 

4. views함수 등록

```python
def line(request):

    seoul=[7.0, 6.9, 9.5, 7.0, 6.9, 9.5, 7.0, 6.9, 9.5, 7.0, 6.9, 9.5, ]
    london=[8.0, 9.9, 12.5, 5.0, 4.9, 3.5, 8.0, 9.9, 4.5, 3.0, 6.9, 2.5, ]
    context={'seoul':seoul,'london':london}

    return render(request,'chart_line.html',context)
```



5. http://localhost:8000/chart/line/
6. ![차트](C:\Users\user\Desktop\차트.PNG)