# proszę to traktować jako dodatek
# uwagi o kopiowaniu służyły tylko uświadomieniu Państwu możliwości zaistneinia takiego problemu

# to ćwiczenie rózni się od tego co robiliśmy na zajęciach

# stworz (dowolną) listę o długości 2 (składjąca się z 2 elemntów)
# i przypisz ją do zmiennej x
lista1 = [2,3]
x = lista1
# przypisz listę x na zmienną y na y[0] oraz y[1]
y = [x,x]
# dodaj element do listy x
x.append(2)
# sparwdz czy y[0] wskazuje na ten sam adres w pamięci komputera co y[1]
# użyj funkcji id()
print(id(y[0])==id(y[1]))

# przypisz listę x na zmienną z[0] i z[1] używajć metody copy() 
z = [x.copy(), x.copy()]
# sparwdz czy z[0] wskazuje na ten sam adres w pamięci komputera co z[1]
print(id(z[0]) == id(z[1]))