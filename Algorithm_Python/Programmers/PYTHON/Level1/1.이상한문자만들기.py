


# 프로그래머스 LV.1 이상한 문자 만들기
# 홀수는 소문자 짝수는 대문자로 만들기





def solution(s):
    answer=[ ]  #답을 담을 변수 생성
    words=s.split(" ")  #s를 뛰어쓰기 기준으로 나눠 word로 분리해야함
    
    for word in words:
        w="" #변환된 문자 w에 저장
        for i in range(len(word)): # 공백기준으로 나뉘어진 word의 길이를 측정
            if i %2:
                w+= w[i].lower()  #홀수는 소문자
            else:
                w+= w[i].upper()  #짝수는 대문자
        answer.append(w) #변환된 값을 answer에 저장
    return ' '.join(answer)   # answer리스트의 각 항복을 묶음.띄어쓰기 있는 문자열 생성





#총 6개의 저장 공간을 만들어 줬다.
#1. s : 입력문장
#2. answer : 최종 답안 넣을 변수
#3. words: 공백기준으로 자른 문장
#4. words: 자른 문장의 문자 덩어리
#5. w: 변환된값 저장할곳
#6. i  : 철자 하나하나 (순서 가리킴)

#몇개의 변수를 생성해야할지 로직을 짜는것도 중요한데, 아직 이것이 미흡하다
# 변수 설정하는거에 망설이지말고 적용해보자!!





            