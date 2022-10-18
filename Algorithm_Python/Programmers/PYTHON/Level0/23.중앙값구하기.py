import numpy as np

def solution(array):
    return np.median(array)


#######
def solution(array):
    array= sorted(array)
    return array[int(len(array)/2)]
