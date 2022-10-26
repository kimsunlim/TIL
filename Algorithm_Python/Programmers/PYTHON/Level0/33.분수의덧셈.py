from fractions import Fraction  #분자 분모 따로 받기 위해 임포트

def solution(denum1, num1, denum2, num2):
    answer=Fraction(denum1,num1)+Fraction(denum2,num2)
    return[answer.numerator, answer.denominator]
    #numerator 분자 , deominator 분모