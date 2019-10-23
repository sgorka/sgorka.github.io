print("Obliczanie wynagrodzenia")
# Spytaj użytkownika o srtawkę godzinową
print("Twoja stawka godzinowa:")
print("Uwaga: liczby zmiennoprzecinkowe wprowadzamy z . np. 2.5")
stawka = input(">") # w tym miejscu python widzi stawka jako napis np. "8".
# sprawdźmy, że tak jest
print(type(stawka))
# Spytaj użytkownika o liczbę godzin pracy dziennie
print("Liczba godzin pracy dziennie:")
godziny = input(">") 

# Oblicz dzienną wypłatę i wyświetl ją użytkownikowi 
# zaokrąglij wynik do 2 miejsc po przecinku 
# uzyj funkcji round
wynagrodzenie = float(stawka) * float(godziny) 
#np. stawka = "8", gdoziny = "2"
#to działa tak, najpierw "8" zamiana na 8.0 oraz "2" zamiana na 2.0
#następnie przypisuje na wynagrodzenie wynik 8*2
#alternatywnie można to zorbić np tak godziny = float(input(">"))
print("Dziennie zarabiasz:", round(wynagrodzenie, 2))
