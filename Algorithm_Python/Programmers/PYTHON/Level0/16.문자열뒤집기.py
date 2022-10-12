def solution(string):
    return string[::-1]
    ##문자열 뒤집는 슬라이싱!!!


def solution(my_string):

    my_list = list(my_string)
    my_list.reverse()

    answer = ''.join(my_list)

    return answer