#01.
#15596번 정수N개의 합

def solve(num_list):
    result =0
    for num in num_list:
        result+=num
        return  result







#02.
#4673전 셀프 넘저

natural_num = set(range(1,10001))  #set함수를 써서 1부터 1000까지 변수를 설정
generated_num =set()

for i in range(1,10001):
    for j in str(i):  #문자열로 바꿔서 하나씩 때준다
        i +=int(j)    #그리고 그 문자들을 다 더한 결과
    generated_num.add(i)

self_num=sorted(natural_num - generated_num)
for i in self_num:
    print(i)




#03.
#1065번 한수

n= int(input())
hansu=0

for i in range(1, n+1):
    if i<100:
        hansu +=1

    else:
        n_str =list(map(int, str(i)))
        if n_str[2]-n_str[1]==n_str[1]-n_str[0]: #인덱스를 지정해줘서 더하기
            hansu +=1
print(hansu)




