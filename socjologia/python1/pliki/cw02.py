imiona = ['Dominika', 'Kamila', 'Nina', 'Julia', 'Konrad', 'Agnieszka', 
	'Klaudia', 'Michał', 'Joanna', 'Kamil', 'Beata', 'Szymon']
	
# dodaj nwoego uczestika zajęć Zbigniew na końcu listy
imiona.append("Zbigniew")
# posortuj listę imiona w porządku alfabetycznym
imiona.sort()
print(imiona)
# usuń ostatnią osobę na liście
imiona.pop() 
# na miejscu 5 dodaj osobę o imieniu Magda
imiona.insert(4, 'Magda') # 5 miejsce czyli 4 index. numerujemy od 0
# rozdziel napis imiona2 używjać metody split() i dodaj uzysjaą w ten sposób listę
# do listy imiona jako kolejne elementy
imiona2 = 'Antonina,Wiktoria,Justyna,Witold,Marianna,Natalia,Sebastian,Błażej,Piotr,Krzystof,Ewa,Agata,Szymon'
imiona2.split(',') # w ten sposób napis imiona 2 zostaje rozdzielnoy, ale tylko w tym miejscu!
print(imiona2)
# aby utrwalic ten wynik i z niego skorzytsać musimy przypisać to na zmienną
imiona3 = imiona2.split(',') 
print('imiona3', imiona3) 
# co więcej dostaliśmy listę
print('imiona3 type', type(imiona3))
imiona.append(imiona3)  # w ten sposób na ostatnim miejscu dodajemy listę
print(imiona) 
# usuńmy ją
imiona.pop()
# sprawdźmy czy zadziałało
print(imiona) 

# rozwiązanie extend
imiona.extend(imiona3)
# sprawdź czy Twoje imię jest na liście używając funkcji in
'Szymon' in imiona
