## Django :파이썬 프레임 워크 

> 웹프레임 워크로 웹이나 어플리케이션을 구출할 수 있는 오픈 소스 프레임 워크



### (1) MVT 패턴

> MVC(model view controller)를 MVT(model,view,template)패턴이라고 한다. 
>
> **Model**은 데이터베이스에 저장되는 데이터를 의미하고, **View**는 실질적으로 프로그램 로직이 동작하여 데이터를 가져와서 적절하게 처리한 결과를 템플릿에 전달하는 역랗을 하고, **Template**는 뷰가 처리한 결과를 받아서 사용자에게 보여주는 UI부분이다.

![장고](C:\Users\user\Desktop\장고.PNG)

**<웹요청 처리 과정>**

1. 클라이언트로부터 요청 -> URLconf 이용하여 URL 분석

2. URL분석결과를 통해 해당 URL 처리를 담당할 View 결정

3. View는 자신의 로직 실행 -> 데이터 베이스 처리가 필요하면 Model을 통해 처리 및 결과 반환

4. View는 로직 처리 후 Template를 사용하여 클라이언트에 전송할 Html파일 생성

5. View는 최종 결과로 Html 파일을 클라이언트에게 보내 응답처리 



### (2) 프로젝트 생성

> 프로젝트 생성 : django-admin startproject djangoWEB

- dir/w

- cd djangoWEB

- **server  실행하는 명령어**: python manage.py runserver

- 사용자 입쟁에서

  - http://localhost:8000/hello/index/

  - http://localhost:8000/hello/hi/

- **Templates**

  - html(tag+text)
  - {{print}}
  - {%동적 코드를 작성하고자 할 때%}
  - {%프리젠테이션 레이어에 로직심을 수 있다%}

  

### (3) Model (ORM)



> 모델 마이크레이션
>
> 사용자 모델 -> DB(테이블)만드는 명령어

 python manage.py makemigrations

 python manage.py migrate

python manage.py createsuperuser

 

 