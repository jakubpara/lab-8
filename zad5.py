import numpy as np
random5x5 = np.random.randint(0,101,size=(5,5))
print(random5x5)

#najwiekszy i najmniejszy element
najwieksza= random5x5.max()
print(najwieksza)
najmniejsza= random5x5.min()
print(najmniejsza)

#najwieksze/najmniejsze elementy w kazdej kolumnie i wierszu
maksymalne_pion=np.max(random5x5,axis=0)
print(maksymalne_pion)
maksymalne_poziom=np.min(random5x5,axis=1)
print(maksymalne_poziom)
#suma wartości w wierszach
suma=np.sum(random5x5,axis=1)
print(suma)