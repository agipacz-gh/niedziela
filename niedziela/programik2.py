liczby =list()
for l in range(2000,3001):
    if ((l%7== 0) and (l%5!= 0)):
        liczby.append(l)
print(liczby)
