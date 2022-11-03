def solution(price):
    answer = 0
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else :
        answer = price

    return int(answer)

    #int 형으로 담아줘야 오류가 안생김 