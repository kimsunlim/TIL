def solution (my_string):
    answer= []  #리스트 형태로 담기

    for i in my_string:
        if i.isnumeric():
            answer.append(int(i)) ##int 형태로 넣어주기!
            answer.sort() #오름차순

        return answer
