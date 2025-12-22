import numpy as np

tabelka = np.zeros((5,5))
tabelka[0,:]=1
tabelka[:,0]=1
tabelka[:,4]=1
tabelka[4,:]=1
print(tabelka)


def zamiana():
    x, y = tabelka.shape
    for i in range(x):
        for j in range(y):
            if tabelka[i,j] ==0 :
                tabelka[i,j] = 1
            else :
                tabelka[i,j] = 0
    return tabelka

print(zamiana())