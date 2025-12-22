import numpy as np
macierz = np.random.randint(1,101, size=(5,5))
print(macierz)

lista=[]

x,y=macierz.shape
for i in range(x):
    for j in range(y):
        if macierz[i,j] >20:
            lista.append(macierz[i,j])
        else:
            pass
a= len(lista)
print(f'liczba wyrazów większych od 20: {a}')
print(f'średnia to: {macierz.mean()}')
