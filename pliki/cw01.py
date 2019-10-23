napis = "welcome"
# dodaj (dowolne) imię do napisu 
napis = napis + ' John'
# Zmień pierwszą literę na dużą
napis = napis.capitalize() # tu zmieniami napis na 'Welcome jihn'
print(napis)
# Zmien wszystkie litery na duże
print(napis.upper()) # tu zmieniami napis na WELCOME JOHN tylko wewnątrz funckji print
print(napis)
# Zamień welcome na hello i przypisz na tą samą zmieną
napis = napis.replace('Welcome', 'hello')
print("\npo zamianie:",napis)
# sprawdźć czy zmienna napis zawiera "welcome"
czy_zawiera = 'welcome' in napis # in zwraca nam true/false
print('\nwynik metody in:', czy_zawiera)
# sprawdźć czy zmienna napis zawiera same litery, użyj metody isalpha
print('wynik metody isaplha', napis.isalpha())


owoce = "gruszka, pomarancza, jablko"
# rozdziel napis owoce używjać metody split(), przypisz wynik na zmieną
# (możesz wypisać wynik tej oepracji by sprawdzić efekt)
owoce2 = owoce.split(',')
print(owoce2)
# sprawdź jaki typ dostaliśmy (uzyj funckji type na wyniku poprzedneigo punktu)
print('typ zmiennej owoce2:', type(owoce2))