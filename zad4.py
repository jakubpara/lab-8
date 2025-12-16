import numpy as np
liczby=np.array( [128, 64, 32, 16, 8, 4, 2, 1])
import random
ndarray=np.random.randint(0,2,size=8)
print(ndarray)

def wartosc_liczby_bin(liczby, ndarray):
    return np.sum(liczby * ndarray)

print(wartosc_liczby_bin(liczby, ndarray))

