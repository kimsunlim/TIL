 #프로그래머스 LV.1  가운데 글자 가져오기
  
  
  def solution(s):
    center= int(len(s)/2)
    
    if len(s)%2 != 0:
      return s[center]  #홀수 일때 가운데 값만 추출
    else:
      return s[center-1:center+1]
