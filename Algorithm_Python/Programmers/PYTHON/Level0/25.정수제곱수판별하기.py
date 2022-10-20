import numpy as np 
def solution (n):
    n=np.sqrt(n)
    if n%1==0:
        return 1
    else:
        return 2