#Super Projekt
import random, time

pytanka1 = [
    ['Na jakim programie transmitowani są Milionerzy?','A:Puls','B:Disney Channel','C:TVN','D:TVP','C'],
    ['Kim byl Karol Wojtyla?','A:Hydraulikiem',' B:Papieżem','C:Strazakiem','D:Nauczycielem','B'],
    ['Ile zawodów wygrał Pudzianowski?','A:18','B:21','C:20','D:19','D'],
    ['Kto rozerwal koszulke Tommy Hilfigera?','A:Rafonix','B:Nitro','C:Gural','D:Oliwka brazil','A']
]

pytanka2 = [
    ['Ile jest pierwiastków na tablicy Mendelejewa?','A:118','B:119','C:117','D:2137','A'],
    ['Ile różnych gatunków kwiatów zostało wymienione w Panu Tadeuszu?','A:2007','B:420','C:2137','D:Nikogo to nie obchodzi','D'] ,
    ['Ile sekund ma godzina?','A:3600','B:60','C:24','D:52','A'],
    ['W ile sekund poziomka wyzerowal denaturat?','A:41s','B:21s','C:68s','D:70s','A']
]

pytanka3 = [
    ['W jakim celu Ryszard zabrał rower?','A:Aby pojechac po papieroski','B:Aby pojechac do mamy','C:Aby pojechac do sklepu','D:Aby go sprzedac','C'],
    ['Czego nie da sie pomalowac?','A:Kamienia','B:Plastiku','C:Drewna','D:Aluminium','D'],
    ['Ile pieniedzy dostal ksieciunio?','A:2zl','B:5zl','C:11zl','D:3zl','A'],
    ['Co zamierzal robic pewien obywatel w sylwestra?','A:Isc spac','B:Imprezowac','C:Zjesc kebaba','D:Grac w gre','D']
]
czy_znasz_odpowiedz=['Jaka jest odpowiedź?','Która odpowiedź jest poprawna?','Poprawna odpowiedź na to pytanie to...','Jak odpowiesz na to pytanie?','Czy znasz odpowiedź?']
poprawna_odpowiedz=['Dobra odpowiedź! Grasz dalej.','Niestety, jest to...poprawna odpowiedź! Gramy dalej.','Tak, to jest dobra odpowiedź!','Tak, to poprawna odpowiedź!','To jest poprawna odpowiedź!','Świetnie, odpowiedziałeś/aś poprawnie!']
gwarantowana = ['5 000','75 000']
czy_chce_kolo_ratunkowe = 'Jeżeli chcesz skorzystać z koła ratunkowego, wciśnij "ratunek" i ENTER. Jeżeli nie, wciśnij ENTER, aby kontynuować. '
lista_wygrane = ['500','1 000','2 000','5 000','10 000','20 000','40 000','75 000','125 000','250 000','500 000','1 000 000']
ilosc_kol = 3
odp=['A','B','C','D','a','b','c','d']
prawdopodobien2 = random.randint(50,100)
p2=round(prawdopodobien2,2)
zdjeciehuberta = 'https://drive.google.com/file/d/14NgX4-vZhNoJ6KAzBjX65j_K2FHCrSEt/view?usp=sharing'
prowadzacy = ['Dobrze Ci idzie!','Świetnie, oby tak dalej.','W takim tempie zaraz dojdziemy do miliona!','Zdenerwowany?','Walczymy dalej!','Jesteś gotowy na następne pytania?']
kolo_ratunkowe = ['1. Telefon do przyjaciela','2. Pytanie do publiczności','3. 50:50']
speed = 'https://drive.google.com/file/d/1OMuzH3gZceKD28iuitglsJff16KBQmgR/view?usp=sharing'

print("db-Dukaty Bydgoskie")
time.sleep(1)
print("Witam Cię programie Milionerzy")
print(zdjeciehuberta)
time.sleep(3)
print('czytam zasady gry:\nw grze są zawsze 4 odp a, b, c, d')
time.sleep(3)
print('W razie wątpliwości, do Twojej dyspozycji są 3 koła ratunkowe:')
print(kolo_ratunkowe[0], kolo_ratunkowe[1], kolo_ratunkowe[2])
print('gotowy/gotowa?\nzaczynajmy, gramy o milion Dukatów Bydgoskich!')
time.sleep(3)
print('Tak przedstawają sie kolejne progi wygranych. Sumy gwarantowane to 5000 db oraz 75 000 db!')
time.sleep(2)
print('=====================')
print('| 12    1 000 000db |')
time.sleep(0.4)
print('| 11      500 000db |')
time.sleep(0.4)
print('| 10      250 000db |')
time.sleep(0.4)
print('|  9      125 000db |')
time.sleep(0.4)
print('|  8       75 000db |')
time.sleep(0.4)
print('|  7       40 000db |')
time.sleep(0.4)
print('|  6       20 000db |')
time.sleep(0.4)
print('|  5       10 000db |')
time.sleep(0.4)
print('|  4        5 000db |')
time.sleep(0.4)
print('|  3        2 000db |')
time.sleep(0.4)
print('|  2        1 000db |')
time.sleep(0.4)
print('|  1          500db |')
print('=====================')
time.sleep(2)

ilosc_pytan = 0
while True:
    if ilosc_pytan < 4:
        print(random.choice(prowadzacy),"\n")
        wylosowane_pytanie = random.choice(pytanka1)
        pytanka1.remove(wylosowane_pytanie)
    elif ilosc_pytan >= 4 and ilosc_pytan < 8:
        print(random.choice(prowadzacy),"\n")
        wylosowane_pytanie = random.choice(pytanka2)
        pytanka2.remove(wylosowane_pytanie)
    elif  ilosc_pytan >= 8 and ilosc_pytan <= 12:
        print(random.choice(prowadzacy),"\n")
        wylosowane_pytanie = random.choice(pytanka3)
        pytanka3.remove(wylosowane_pytanie)
        if ilosc_pytan == 12:
            print("GRATULACJE!\nWYGRAŁEŚ 1 000 000 Dukatów Bydgoskich!")
            break
    print(wylosowane_pytanie[0])
    print(wylosowane_pytanie[1],wylosowane_pytanie[2],wylosowane_pytanie[3],wylosowane_pytanie[4])
    wygrana = lista_wygrane[0]
    if len(kolo_ratunkowe)>0:
        print(czy_chce_kolo_ratunkowe)
        odp_na_kolo_ratunkowe = str(input())
        if odp_na_kolo_ratunkowe == 'ratunek':
            print('Zdecydowałeś się na użycie koła ratunkowego. Z którego koła chcesz skorzystać?\nAby wybrać, wciśnij odpowiednią cyfrę.')
            print('Dostępne koła ratunkowe:',kolo_ratunkowe)
            ktore_kolo = str(input())
            if ktore_kolo == '1':
                print('\nDzwonimy do Twojego przyjaciela.')
                print('Hubercik: Witaj! Z tej strony Hubert Urbański z Milionerów.\nTwój przyjaciel gra właśnie o milion i potrzebuje Twojej pomocy przy pytaniu.\nMasz do dyspozycji 4 odpowiedzi.\nP: Myślę, że poprawna jest odpowiedź',wylosowane_pytanie[5],'i jestem tego pewny na', p2,'%. Mogę się jednak mylić...\n')
                kolo_ratunkowe.remove('1. Telefon do przyjaciela')
            elif ktore_kolo == '2':
                print('\nProszę publiczność o zagłosowanie na poprawną państwa zdaniem odpowiedź.\nOto wyniki procentowe kolejno dla odp A, B, C i D:')
                A = random.randint(5,95)
                B = random.randint(5,95)
                C = random.randint(5,95)
                D = random.randint(5,95)
                while (A+B+C+D)!=100:
                    A = random.randint(5,95)
                    B = random.randint(5,95)
                    C = random.randint(5,95)
                    D = random.randint(5,95)
                    if wylosowane_pytanie[5]=='A':
                        while A<=B or A<=C or A<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='B':
                        while B<=A or B<=C or B<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='C':
                        while C<=B or C<=A or C<=D:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                    elif wylosowane_pytanie[5]=='D':
                        while D<=B or D<=C or D<=A:
                            A = random.randint(5,95)
                            B = random.randint(5,95)
                            C = random.randint(5,95)
                            D = random.randint(5,95)
                print(A, B, C, D)
                kolo_ratunkowe.remove('2. Pytanie do publiczności')
            elif ktore_kolo == '3':
                if wylosowane_pytanie[5] in odp:
                    odp.remove(wylosowane_pytanie[5])
                print('\nProszę o odrzucenie 2 błędnych odpowiedzi.\nDo wyboru pozostały:',wylosowane_pytanie[5],'i',random.choice(odp))
                print()
                kolo_ratunkowe.remove('3. 50:50')
            ilosc_kol -= 1
            print('Pamiętaj - ilość pozostałych kół ratunkowych to:', ilosc_kol)    
    time.sleep(1)
    print(random.choice(czy_znasz_odpowiedz))

    odpowiedz = str(input()) 
    odpowiedz1 = odpowiedz.capitalize()

    if odpowiedz1 == wylosowane_pytanie[5]:
        print(random.choice(poprawna_odpowiedz),'Twoja wygrana to',wygrana,'złotych.')
        if wygrana == '5 000' or wygrana == '75 000':
            print("\nKwota, którą właśnie wygrałeś to kwota gwarantowana.\nOznacza to, że nawet w przypadku przegranej, będziesz mógł zabrać te pieniądze do domu.")
        print()
        time.sleep(1)
        lista_wygrane.remove(wygrana)
        ilosc_pytan = ilosc_pytan+1
   
    else:
        print("Niestety, odpowiedź której udzieliłeś była niewłaściwa. Poprawna odpowiedź to",wylosowane_pytanie[5])
        if ilosc_pytan>3 and ilosc_pytan<8:
            print("Niemniej jednak, ponieważ dotarłeś do progu kwoty gwarantowanej, twoja wygrana wynosi",gwarantowana[0],", więc nie wychodzisz z pustymi rękoma! Gratuluję!")
        else:
            print("Niemniej jednak, ponieważ dotarłeś do progu kwoty gwarantowanej, twoja wygrana wynosi",gwarantowana[1],", więc nie wychodzisz z pustymi rękoma! Gratuluję!")
        print("Dziękujemy za udział w grze!")
        break