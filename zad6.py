import numpy as np

tablica= np.zeros((3,3))
print(tablica)

tablica[2,:]=1
print(tablica)

tablica= np.zeros((3,3))
tablica[1:3,1]=1
print(tablica)

tablica= np.zeros((3,3))
tablica[1:3,:]=1
print(tablica)

tablica= np.zeros((3,3))
tablica[0:2,0]=1
tablica[0:2,2]=1
print(tablica)

tablica= np.zeros((3,3))
tablica[1:3,1:3]=1
print(tablica)

