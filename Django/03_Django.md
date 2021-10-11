## 3.Django (modify, json)



#### 1.Modify

>  **ModifyForm 이벤틀 발생시 생각?**

1)수정 할수 있는 페이지로 이동

**urls**: path등록

**->**

**view **

**게시물 id 서버로 전송->model**

**render ->template (modify.(modify.html),context)**

```python 
def bbsModifyForm(request):
    id=request.POST['id']

    #model
    board=Bbs.objects.get(id=id)
    context = {'board': board,
               'name': request.session['user_name'],
               'id': request.session['user_id']}

    return render(request,'modify.html',context)
```





> **modify**

1) urls  : path 등록

2) views

- id, title, content

```python 
def bbsModify(request):
	id = request.POST['id']
	title = request.POST['title']
	content = request.POST['content']
```



 **update table set where**

```python
update table set attr = value where id = 1
 obj = modelName.objects.get(id=1)
 obj.attr = '변경'
  obj.save() -- commit
```

- model(update)
- render X

- redirect('bbs_list')

```python
board =Bbs.objects.get(id=id)
    board.title=title
    board.content=content
    board.save()
    
     return redirect('bbs_list')
```



#### 2. Json : python 형태의 딕셔너리



> **JSON은 자바스크립트의 객체 표기법으로부터 파생된 부분 집합이다.**
>
> 데이터를 저장하거나 전송할때 많이 사용되는 경량의 DATA 교환 형식

 

1. JSON 데이터는 **name-value** 이름과 값의 쌍으로 이루어진다.

2. JSON 데이터는 쉼표(,)로 나열된다.

3. 객체(object)는 중괄호({})로 둘러쌓아 표현한다.

4. 배열(array)은 대괄호([])로 둘러쌓아 표현한다.



```python
**ajax 통신 -json**
$.ajax({
   url:"{% url 'bbs_search' %}",
   type:"post",
   data:{'csrfmiddlewaretoken':'{{csrf_token}}'},
   dataType:"json",
   success:function(data){
      alert(data)
   }
})
```



+json.dumps(dict): 딕셔너리를 제이슨으로 바꾸는것





> 패턴

```python
select*from table where title like '_____%'
select*from table where title like '_____%'
 ->modelName.objects.filter(subject_startswith='공지')
    
    
    
     if type =='title':
        boards=Bbs.objects.filter(title__startswith=keyword)

    if type =='writer':
        boards = Bbs.objects.filter(writer__startswith=keyword)
    print("ajax--result:",boards)
    
    
   data =[]
    for board in boards:
        data.append({
            'id'    :board.id,
            'title' :board.title,
            'writer':board.writer,
            'regdate':board.regdate,
            'viewcnt':board.viewcnt,
        })

    return JsonResponse(data, safe=False)
```

