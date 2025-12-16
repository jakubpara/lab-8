import matplotlib.pyplot as plt
kategorie=['Telefony', 'telewizory', 'komputery', 'drukarki']
wartosci=[31,12,18,9]
plt.bar(kategorie,wartosci, color=[ 'red', 'blue', 'green', 'yellow'])
plt.title('Ilość sprzedanych produktów')
plt.xlabel('Kategorie')
plt.ylabel('Wartości')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
