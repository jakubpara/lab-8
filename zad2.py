import matplotlib.pyplot as plt

Kategorie=['owoce', 'warzywa', 'śłodycze', 'picie']
wartosci=[24,12,18,16]
plt.pie(wartosci, labels=Kategorie, autopct=lambda p: p*100, startangle=90,
        colors=('red', 'green', 'lightblue', 'yellow'))
plt.title('Udział w sprzedaży')
plt.show()