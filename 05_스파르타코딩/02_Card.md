# 새해 카드





### 1. 봉투 html 만들기



1. 제목을 지정
2. body 안에 색상지정
3. 첫번째 클래스 **.envelope**  : 봉투 url넣고 가운데 위치 조정
4. 두번째 클래스 **.envelope-msg**  :글씨넣기

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2021 새해!!</title>
    <style>
        body{
            background-color: #9b070f;     #색상지정
        }

        .envelope{				      	  #첫번째 클래스
            
            
            width: 200px;
            height:200px;

            background-image:					 #이미지url넣기
            url(https://pngimg.com/uploads/envelope/envelope_PNG18366.png);
            background-size: cover;
            background-position: center;  #가운데

            margin: 200px auto 0px auto;	#가운데 여백을 통해 지정



        }

        .envelope-msg{					#두번째 클래스 
            color: white;
            text-align: center;    
        }

```



-body에 2개 클래스 

```python
   </style>

</head>
<body>
    <div>
        <div class="envelope"></div>     #첫번째 클래스
        <h2 class="envelope-msg">선림이가 만든 봉투를 열어봐^___^</h2> #두번째 클래스


    </div>>
    
    
</body>
</html>
```







### 2. 편지 html 만들기

1. 기존 봉투html 숨기기 위해 body에서 클래스 지정

```python
<body> 
    <div class ="letter-close">   #클래스 지정
        <div class="envelope"></div>
        <h2 class="envelope-msg">선림이가 만든 봉투를 열어봐^___^</h2>


    </div>



    <div class="rtan"></div>  #르탄이 클래스
        
</body>
```



2. style에서 봉투html 숨기기
3. 르탄이 이미지 넣고 위치 조정



```python
.letter-close{
            display:none;                #기존 봉투html숨김
        }

        .rtan{								#르탄이 클래스 지정
            background-color: white;

            width: 200px;
            height: 200px;


            background-image: url('https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/xmas/rtan.gif');
            background-size:cover;
            background-position: center;

            margin:100px auto 0px auto;

            border-radius: 100px;				  #겉면 둥글게 만들기

            border: 5px solid white;              #겉면 색깔
            box-shadow: 0px 0px 10px 0px white ;  #겉면 그림자 효과
            
            
        
        }

    </style>
```





4.messagebox생성

```python
<div class="letter-open">

        <div class="rtan"></div>
        <h1>모두들 2020년 수고많았어요.</h1>
        <div class="messagebox">
        친구들에게. <br />
        올해 이런저런 일이 많았는데 <br />
        너희 덕분에 하나도 힘들지 않았어 <br />
        내년에도 우리 우정 변치말자 <br />
        연말에 다 같이 못 봐서 아쉽다 <br />
        <p class="from">2020.12.31 깜띡이 선림이가</p>

        </div>
```



5.messagebox 스타일

```python
 .messagebox{
            background-color: ivory;

            width: 400px;
            margin: auto;
            color:brown;
            padding: 30px;
            font-size: 20px;
            line-height: 30px;

            box-shadow: 0px 0px 10px 0px white ;


        }

        .from{
            text-align: right;
            margin-bottom: 0px;

        }
```





### 3. 모바일 버전처리

- 크롬 F12들어가서 핸드폰 아이콘 클릭
- Responsive 365*645지정



```python
 @media screen and (max-width: 760px) {
            .messagebox{
                width: 300px;
                height: 20px;
            }
            .rtan {
               
                width: 150px;
                height: 150px;
                margin: 70px auto 0px auto;
                
            }
            .h1{
                font-size: 28px;
            }
            .envelope{
                margin: 150px auto 0px auto;
            }

        }
```



### 4. 간단한 자바스크립트

- 스타일 밑에 script생성

```python
 <script>
        function open_letter() {
            document.getElementsByClassName("letter-close")[0].style.display = 'none'
            document.getElementsByClassName("letter-open")[0].style.display = 'block'

        }
    </script>
```





### 5. 눈오는 효과

- title밑에 자바 스크립트 코드 복붙!

```python
<script src="https://s3.ap-northeast 2.amazonaws.com/materials.spartacodingclub.kr/xmas/snow.js"></script>
```





### 

<img src="C:\Users\김연희\Desktop\TIL\05_스파르타코딩\img_s\card.png" alt="card" style="zoom:25%;" />



<img src="C:\Users\김연희\Desktop\TIL\05_스파르타코딩\img_s\card2.png" alt="card2" style="zoom:30%;" />