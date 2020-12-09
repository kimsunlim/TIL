## 2. Django :파이썬 프레임 워크 (2일차)

#### process



> **프로젝트 생성**

1. **Terminal**창에서 dir/w로 살펴본뒤,

   **python manage.py startapp pullsApp** 앱만들기->프로젝트 창에 생성

2. **dangoweb**의 settings창에 **pullsApp등록!**

3. pullsApp에 urls 생성

``` python
from django.contrib import admin
from django.urls import path , include
from pullsApp    import views

urlpatterns = [
    path('index/', views.index,name='index'),
```



4.**views**창

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse ('테스트 링크')
```

5.Terminal 에서 **python manage.py runserver **서버 실행

6.윈도우 창에 http://localhost:8000/pulls/index/ 확인!





---

> **모델생성**

1.pullsApp의 **models** 창에서 모델생성

```python
from django.db import models

# Create your models here.

class Question (models.Model):
    question_text=models.CharField(max_length=200)
    regdate      =models.DateTimeField()

    def __str__(self):
        return self.question_text+" , "+self.regdate
#객체의 문자열을 받는 함수

class Choice (models.Model):
    question =models.ForeignKey(Question,on_delete =models.CASCADE())
    choice_text=models.CharField(max_length=200)
    votes      =models.IntegerField(default=0)
   
   
    def __str__(self):
        return self.question +","+ self.choice_text +","+           str(self.votes)
```





2.**admin**

```python
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)

## 생성한 모델을 추가해야함
```



- **Terminal**마이그레이션 해야함
  -  python manage.py makemigrations
  -  python manage.py migrate
  - python manage.py  runserver



3. **templates**디렉토리 생성 ->**pulls**디렉토리 생성->**index html**생성

   ```python
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
   </head>
   <body>
       {%if lists%}
       <ul>
           {%for question in lists%}
           <li><a href="">{{question.question_text}}</a></li>
           {%endfor%}
       </ul>
       {%else%}
       <p>데이터가 존재 하지 않습니다~~</p>
       {%end if%}
   </body>
   </html>
   ```

   

   

> view 참고

```python
#select *from table;
    # ->modelName.object.all()

    #select*from table where id=1;
    #->modelNAme.objects.filter(id=1)

    # select*from table where id=1 and pwd=1;
    # ->modelNAme.objects.filter(id=1,pwd=1)

    # select*from table where id=1or pwd=1;
    # ->modelNAme.objects.filter(Q(id=1)|Q(pwd=1))

    # select*from table where subject like %공지%;
    #->modelName.objects.filter(subject_icontains='공지')

    # select*from table where subject like 공지%;
    # ->modelName.objects.filter(subject_startswith='공지'

    # select*from table where subject like %공지;
    # ->modelName.objects.filter(subject_endswith='공지')

 #insert into table values('')
    #model(attr=value,attr=value....)
    #->model.save()

    #delete *from table where id=1
    #->modelName.odjects.get(id=1).delete()

    #update table set attr=value where id=1
    #obj=modelName.objexts.get(id=1)
    #obj.attr='변경'
    #obj.save() --commit
```





#### 웹링크 구현

1. index.html 변경

   ```python
   <li><a href="../{{question.id}}">{{question.question_text}}</a></li>
   ```

2. urls로 받아야함(패턴에 추가)

   ```python 
   path('<int:question_id>/', views.choice,name='index'),
   ```

 3.view 함수생성(**get_object_or_404** import 하기)

```python
def choice(request,question_id):
    print('param question_id',str(question_id))
    list=get_object_or_404(Question,pk=question_id)
    print("-"*100)
    print(lists)
    print("-"*100)
    context={'clsits':lists}
    return render(request,'pulls/choice.html',context)

```

 4.pulls 에 choice html만들기 (body 부분)

```python
<h1>{{clist.question_text}}</h1>
    <hr/>
    <form method="post" action="{%url 'vote'%}">
    {% csrf_token %}
    {%for choice in clist.choice_set.all%}
    <input type="radio"
           name="choice"
           value="{{choice.id}}"
            >
    <label>{{choice.choice_text}}</label><br/>
    {%endfor%}
    <p>
            <input type="submit" value="VOTE">
        </p>
    </form>

```



5.pulls 에 result html만들기

6.views다시가서 함수생성





> static 파일을 한곳으로 모을때:**python manage.py collectstatic**

**{% load static %}**





---



------------------------------home.html

{%include 'header.html' %}

{%block content%}

/<section></section>

{%endblock%}

{%include 'footer.html' %}