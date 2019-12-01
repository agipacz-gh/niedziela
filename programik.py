
print('Wejscie: ')
wartosci=input()

lista = wartosci.split(",")
print(lista, type(lista))
#for i in range(len(lista)):

    #lista[i] =int(lista[i]) to jest to samo co w linijce 11 tylko
    #szybciej

lista = [int(i) for i in lista]
print(lista, type(lista))

#Dopisz konwersj int przy uzyciu funkcji map()

lista = list(map(int,lista))
