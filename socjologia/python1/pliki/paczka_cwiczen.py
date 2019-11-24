'''Celem tej paczki zajęć jest dostarczenie Wam materiału do powtórzenia dotychczasowego materiału. Kolejne ćwiczenia odnoszą się do kolejnych elementów, których się uczyliśmy'''

# CZĘŚĆ 1. Instrukcje warunkowe

# Zasadnicza funkcja instrukcji warunkowych jest prosta: dzięki nim komputer podejmuje decyzje według zasad, które mu podamy. Przykład:

pogoda = 'pod psem'

if pogoda == 'pod psem':
	print('lepiej zostań w domu')
elif pogoda == 'znośna':
	print('od biedy można się ruszyć')
else:
	print('spoko, możesz wyjść')

# Ten program zaleci użytkownikowi, czy w danej pogodzie jest sens wyjść na dwór. Spróbuj zmienić wartość zmiennej pogoda na 'znośna' albo coś innego i zobacz, jaki będzie skutek.

# Ten program można z łatwością rozbudować o element interaktywności. W takim wariancie będzie pytał użytkownika, jaka jest pogoda, a potem reagował na odpowiedź.

pogoda = input('jaka jest pogoda? ')

if pogoda == 'pod psem':
	print('lepiej zostań w domu')
elif pogoda == 'znośna':
	print('od biedy można się ruszyć')
else:
	print('spoko, możesz wyjść')

# Zadanie 1.1: Zbuduj aplikację, która zapyta użytkownika (za pomocą inputa), jaki ma nastrój. Następnie niech przeanalizuje odpowiedź użytkownika i na tej podstawie udzieli mu rekomendacji utworu muzycznego dopasowanego do jego nastroju. Ja, przykładowo, kiedy ogarnia mnie melancholia, puszczam sobie smutne kawałki na pianinku. Co poleci Twoja aplikacja? Twój wybór. A może wydrukuje nawet link do odpowiedniego kawałka na jutubie? To by było coś!


# Zadanie 1.2*. Wymaga odrobiny pomyślunku. Zachęcam do pokombinowania:

# Z wykorzystaniem takich inputów i instrukcji warunkowych, można skonstruować kalkulator. I to jest Twoje zadanie! Zbuduj aplikację, która przyjmie od użytkownika wartości zmiennych liczba1 i liczba2, a także informację na temat tego, jakie działanie ma na nich wykonać – dodawanie, odejmowanie, mnożenie czy dzielenie. Następnie niech program wykona żądane przez użytkownika działanie.

# Polecam też, żebyście wrócili do zadania, które po podaniu przez użytkownika informacji na temat temperatury i opadów doradzała, czy należy założyć kurtkę i czapkę.



# CZĘŚĆ 2. PĘTLA WHILE

# Pętla WHILE służy do tego, by określone czynności były wykonywane tak długo, jak długo spełniony jest postawiony warunek.

# Przykładowo pętla:

while x < 2:
	print(x)

# będzie wykonywała drukowanie wartości zmiennej x tak długo, jak x jest mniejszy od dwóch.

# Często budujemy pętlę WHILE, która posługuje się odliczaniem. W ten sposób regulujemy, jak wiele razy pętla ma zostać wykonana.

# Przykład:

x = 1

while x < 5:
	print(x)
	x += 1

# Zadanie 2.1. Zbuduj pętlę, która wydrukuje wszystkie wartości z zakresu 1-15.

# Zadanie 2.2. Zbuduj pętlę, która wydrukuje CO DRUGĄ wartość z zakresu 1-20.

# Zadanie 2.3. Zbuduj pętlę, która wydrukuje PODZIELNE PRZEZ 3 liczby z zakresu 1-20. W tym celu posłuż się działaniem MODULO (%).

# Przypomnienie, jak działa MODULO, znajdziecie np. tutaj: https://www.learnpython.org/pl/Podstawowe_operatory
# Zajrzyjcie też do zadań, które wykonywaliśmy na zajęciach.

# Przypominam Wam też PRAWDOPODOBNIE NAJŚMIESZNIEJSZY ŻART PROGRAMISTYCZNY, JAKI KIEDYKOLWIEK ZOBACZYCIE:

haslo_uzytkownika = input('powiedz "krowa" ')
while haslo_uzytkownika != 'krowa':
	haslo_uzytkownika = input('powiedz krowa ')

print('brawo! dokładnie tak chciałem')

# Ten przykład jest dość kształcący. Pozwala zauważyć, że pętla może być wykorzystana do tego, by nieustannie zadawać użytkownikowi pytanie tak długo, jak nie udziela odpowiedzi, której oczekujemy. Stąd:

# Zadanie 2.4. Wróć do programu polecającego utwory muzyczne dopasowane do nastroju opisanego w zadaniu 1.1. Posiłkując się powyższym żartem programistycznym, zbuduj program, który będzie pytał użytkownika o nastrój. Niech ma możliwość odpowiedzi 'dobry', 'średni', 'kiepski'. Kiedy użyje innej odpowiedzi, niech program mu nie odpuszcza, tylko ponowi pytanie.

# W tym celu mogą przydać się Wam operatory AND i OR, które omawialiśmy przy przykładach z temperaturą, opadami, kurtką i czapką.
# Kapsułkowe podsumowanie operatorów logicznych w Pythonie znajdziecie tutaj:
# https://www.w3schools.com/python/python_operators.asp

# CZĘŚĆ 3. PĘTLA FOR

# Pętla FOR służy do tego, by wykonywać czynności na kolejnych elementach zbiorów. Na przykład list:

przykladowa_lista_liczb = [1,2,3,4,5,6]
przykladowa_lista_imion = ['Jarek', 'Kasia', 'Alicja']

# Przykłady działania pętli FOR

for liczba in lista_liczb:
	print (liczba*2)

for imie in lista_imion:
	print('Cześć, ' + imie)

# w pętli FOR można też wprowadzać bardziej skomplikowane operacje. Można na przykład zbudować funkcję FOR, która policzy wszystkie parzyste liczby w podanym zbiorze. Weźmy na warsztat listę przykladowa_lista_liczb, którą wprowadziliśmy wcześniej. I policzymy występujące w niej liczby parzyste z wykorzystaniem MODULO.

liczba_liczb_parzystych = 0
for liczba in przykladowa_lista_liczb:
	if liczba % 2 == 0:
		liczba_liczb_parzystych += 1

print(liczba_liczb_parzystych)

# Posiłkując się tym przykładem, zrób kolejne zadanie.

# Zadanie 3.1. Korzystając z pętli FOR i instrukcji warunkowych, zbuduj pętlę, która policzy, ile osób w wieku poniżej 19 lat wzięło udział w konferencji. Pomoże Ci przykład powyżej.
# Wiek kolejnych uczestników naszej wyimaginowanej konferencji podany jest w liście poniżej:

wiek_uczestnikow_konferencji = [20,13,16,21,22,21,19,18,17,16,30]

# Zadanie 3.2. Z gwiazdką, ale malutką. Z pewną dozą prawdopodobieństwa możemy przyjąć, że kobiece nazwiska kończą się na literę 'a'. Korzystając z pętli FOR, oblicz, ile nazwisk na podanej niżej liście nazwisk to nazwiska żeńskie. Uwaga, pomocna może być następująca technika:

slowo = 'konik'
ostatnia_litera_slowa = slowo[-1]
print(ostatnia_litera_slowa)
# taka konstrukcja wydrukuje nam ostatnią literę stringa przechowywanego w zmiennej slowo

lista_nazwisk = ['Kowalska', 'Szczepański', 'Wiktorski', 'Brzęczyk', 'Karwacki']

# Jako zadania z gwiazdką, przypominam zadania, które przekazałem Wam wcześniej, i którym część z Was podołała. Wymaga sporo kombinowania. Jest tu do rozwiązania problem wymagający pomyślunku. Warto spróbować.

# Zadanie 2.4. Lista bitcoin_prices, którą podaję Wam poniżej, zawiera kursy bitcoina na zamknięcie dnia z okresu 30.10.2019-28.10.2019. Waszym zadaniem jest wykorzystać pętlę FOR i instrukcje warunkowe w taki sposób, żeby przypisać do zmiennych i wydrukować:
# 	1. Najwyższy kurs bitcoina w tym czasie
# 	2. Najniższy kurs bitcoina w tym czasie

# 	Da się to zrobić, poprzez funkcje MAX i MIN:
# 	max(bitcoin_prices)
# 	min(bitcoin_prices)

# 	Ale my jesteśmy ambitni i zrobimy to na piechotę ;) Da się to zrobić, korzystając wyłącznie z poleceń, które już znacie. Wymaga tylko trochę kombinowania ;)

# ################### #
# I teraz zadanie Z WIELKĄ GWIAZDKĄ! Proszę, byście na podstawie podanych wartości kursu bitcoina, pętli, warunków, przypisywania zmiennych, napisali program, który obliczy najdłuższą hossę i najdłuższą bessę w podanym przedziale wartości kursu bitcoina. Chodzi o najwyższą liczbę dni, przez które kurs rósł i najwyższą liczbę dni, przez które kurs spadał.

# Zastanów się, jak rozwiązać to zadanie. Jeśli nie uda Ci się wymyślić rozwiązania, możesz pomóc sobie wskazówkami zamieszczonymi poniżej. W takim wypadku skup się na tym, żeby zrozumieć, co się tam dzieje! To jest najważniejsze.


# PODPOWIEDZI DO ZADANIA Z GWIAZDKĄ:

current_max_value = bitcoin_prices[0]
# to jest komenda na odczytywanie wybranego elementu z listy. Tutaj to element zerowy, czyli pierwszy – taka to cudaczna zasada, że elementy listy liczy się od zera

# tutaj buduję wstępne zmienne, któ®e potem będę modyfikował
rekord_dlugosci_hossy = 0
rekord_dlugosci_bessy = 0

dlugosc_hossy = 0
dlugosc_bessy = 0


# tutaj buduję pętlę, która czyta kolejne wartości i porównuje je z wcześniej zbadanymi. Jeśli obserwuje hossę, zwiększa zmienną reprezentującą jej długość.
for element in bitcoin_prices:
	if element > current_max_value:
		dlugosc_hossy += 1
		current_max_value = element
		if dlugosc_hossy >= rekord_dlugosci_hossy:
			rekord_dlugosci_hossy = dlugosc_hossy
	else:
		dlugosc_hossy = 0

print (rekord_dlugosci_hossy)


# Obiecana w zadaniu lista bitcoin_prices:

bitcoin_prices = [6276.4644997238,6321.713671307,6341.0948126498,6360.1412719216,6344.7389429436,6405.1397546807,6396.3521235412,6425.9178018185,6514.4894527375,6412.524289058,6343.6325037562,6365.655231516,6327.4806461044,6327.1546960646,6282.4386771629,5524.8010934193,5511.1528335321,5448.6006335653,5497.4112787322,5553.014895008,4800.3428974568,4246.3127740611,4478.2995582941,4405.7440313629,4329.9172203207,3728.8726484882,3951.20502915,3640.5571648024,3792.1923641199,4174.31997237,4218.6083631146,3952.4478953992,4178.60382773,4118.5182417699,3847.0327374089,3889.2921196935,3713.5733827508,3578.2066240384,3391.8741459694,3452.6161853921,3507.3063671956,3419.7337684576,3360.9466282566,3414.8337488292,3263.5479129873,3212.207080727,3194.96227244,3200.6424680869,3478.461202649,3562.8949463603,3709.3167592101,4065.7999528499,3824.7397939051,3862.7263286473,3949.7943416583,4054.2962598168,3767.3500239009,3807.1530224727,3587.1982229208,3865.5293004371,3689.5646203364,3715.5644411293,3882.304754348,3795.5927412969,3812.3811076791,3809.9143429619,4014.1331870739,3989.6317409326,3992.9861439065,3995.3251931641,3617.3462911588,3606.1648903844,3611.5282378524,3497.6693915005,3654.3470673605,3568.7512587366,3593.7217397683,3623.717336702,3605.8551868777,3690.9085636878,3544.2217242808,3528.4635294479,3581.5519472363,3549.770799097,3562.9204764613,3566.6661636996,3563.2780095528,3539.6209472447,3425.2621611882,3395.0186452497,3441.0322154158,3420.633226576,3439.8056988758,3433.0352852216,3404.499313399,3412.2304311019,3419.7678987458,3367.5190315823,3360.534075862,3591.0221518825,3617.4646801319,3621.1540027134,3593.1831765659,3579.3418810265,3569.5548327757,3558.3968581047,3566.2477646317,3596.4051912371,3606.1519884106,3865.3181649793,3904.4829202328,3924.7398439211,3889.7584851849,3933.6075896328,4105.1127585961,3763.6205157956,3819.8653414425,3797.5817895103,3772.9363353275,3799.678542951,3811.6119793671,3804.4191701095,3782.6641011218,3689.8628931904,3832.0808847342,3848.9563696825,3859.8399833296,3828.3719040694,3898.8684595605,3899.6558689562,3851.2491896498,3866.2959463248,3846.2744415121,3855.7443626577,3892.0523011383,3985.8512364813,3970.3890446061,3974.4157640954,3996.037130764,4027.7873954939,3974.8114294551,3987.3052249052,3977.707443288,3968.4387009854,3913.7817170518,3915.3753197805,4018.5905096995,4008.3708718477,4080.2601141916,4081.2216046987,4094.7047913777,4135.1849399747,4818.7706353498,5102.1507526415,4875.5994313973,5030.9332705867,5028.3210819427,5198.1731702888,5260.2050430865,5179.997649218,5283.543757825,5049.6058235388,5077.5158640878,5066.8670401606,5158.3874010066,5045.6751659083,5184.2044677779,5220.9599338197,5276.5589823291,5266.6612458779,5292.1483296981,5276.5583181647,5398.4334166027,5552.5219105461,5432.9910174238,5132.227526274,5151.5745281681,5200.1932393191,5152.5457396305,5151.4334996793,5277.4444688896,5297.9424922151,5405.8780670084,5697.6790537992,5812.3317793033,5713.0350518135,5706.0084207883,5899.5296934602,5932.4413913918,6159.6859018287,6387.829450439,7254.8055361621,6992.7066614624,7906.9408350528,7928.4174163467,8177.4535191838,7820.0762428219,7243.650538964,7295.6497288231,8221.2593953546,7917.0124987984,7961.1287431622,7723.9038796248,7903.8469103955,8038.5067907549,8089.5701634982,8653.1423680221,8800.3466061527,8719.3314849999,8672.4001072907,8287.0402563223,8513.2038819334,8588.4795049694,8744.2655607165,8474.0482291229,7645.5725139007,7790.3211349552,7730.8817258862,8030.2560794416,7949.425798625,7600.9224920885,7954.0062377205,7903.6252503798,8151.7886797815,8256.7200994618,8667.7879539941,8836.1684129096,9061.5404606385,9346.9750871976,9012.4878496522,9259.1236383919,9559.9006885716,9906.407965055,10461.4121688088,10843.5709747797,10996.4597495353,11665.4096837335,12444.9258599878,11086.2688286526,12316.9530120207,12024.0809722046,10932.3105071733,10454.6838183291,10800.1301399504,11942.2402247929,11645.5246063376,10946.2090547386,11219.0460004352,11422.1144680283,12335.9993946484,12575.904067439,12054.1837934894,11324.1446969751,11802.9599635884,11279.6027356333,10506.3958273087,10934.4827395525,9490.4105157548,9733.1321340919,10603.3488731713,10466.2609381509,10983.2160020296,10551.1316333347,10285.6392306749,10027.5326122485,9771.5047613175,9897.4293515161,9812.2263505784,9440.1400373076,9495.855261405,9506.704273142,9572.735371803,10005.2944733245,10385.2006061246,10513.9114715942,10831.2598554087,10985.8075416287,11811.7870541507,11310.187223605,11956.0472230184,11817.4554825164,11827.5745716918,11278.2812549022,11485.3657829898,11391.9686539038,10869.3791128623,10211.4985816982,10386.5395500195,10388.4505925604,10212.1014417394,10335.3728385716,10774.8103058331,10818.5070076193,10064.9167944793,10161.1647494901,10364.2813536875,10171.4974606754,10068.922419922,10312.2150398496,10122.1965329581,9743.1620510451,9487.9764335192,9590.7363369227,9624.9839105321,9780.6678970327,10381.8559592516,10691.31129913,10555.0469008368,10576.3178915251,10334.0238858467,10495.2273642085,10402.7965306911,10332.9421881057,10082.9468264833,10152.7529840771,10396.7672047403,10299.4769604855,10351.2320218437,10302.1907136783,10301.6596516938,10231.4215119596,10168.2877093815,10223.5055788024,10138.3352052234,9984.520515967,10031.8667089936,9719.7186961077,8688.9735259572,8438.7085524873,8103.2108995944,8195.2106969967,8146.4140320046,8085.7132904218,8241.3414700027,8333.6891904217,8273.4640176573,8203.8438327979,8163.9026381024,8137.1466890387,7853.6933048347,8236.2083793045,8201.6378181926,8572.3808124348,8582.1445177037,8320.1715813968,8328.6042603935,8282.1773258265,8337.8189985374,8003.8203947876,8058.0580811125,7970.2394756046,7943.3471070605,8200.3187633988,8200.2460994923,8073.4095438836,7420.4158364928,7460.6174159279,8591.2238974163,9171.3065318558,9578.3675560737,9458.2233596272]

