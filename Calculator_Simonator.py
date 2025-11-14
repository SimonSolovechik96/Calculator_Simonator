
# geometrinės formos kūno ploto skaičiuoklė
print("Kokio geometrinės formos kūno plotą nori paskaičiuoti? ")

area = input ( " Pasrink formą ( kvadratas, stačiakampis, skritulis, trikampis)")
if area == 'kvadratas':
    kraštine = float (input ("įvesk kraštinės ilgį: "))
    plotas = float (kraštine**2)
    print ("Tavo Rezultatas:") 

    print( plotas)
elif area == 'skritulis':
    choice =  input ("Nori įvesti skersmenį ar spindulį? (skersmuo/spindulys):")
    if choice == "spindulys":
        r = float(input("Įvesk spindulį:"))
        plotas = float(3.14*r**2)
        print ("Tavo Rezultatas:")
        print (plotas)
    elif choice == "skersmuo":
        d = float(input("įvesk skersmenį:"))
        plotas = float(3.14*d)
        print (plotas)
elif area == 'stačiakampis':
    A_kraštine = float ( input ("įvesk kraštinės ilgį: "))
    plotis = float ( input ("įvesk kraštinės plotį: "))
    plotas = A_kraštine * plotis
    print ("Tavo Rezultatas:")
    print (plotas)
elif area == 'trikampis':
    pagrindas =  float ( input ("įvesk pagrindo ilgį:"))
    aukštis = float ( input ( "įvesk trikampio aukštį:"))
    plotas = 1/2*pagrindas*aukštis
    print ("Tavo rezultatas:")
    print (plotas)

else: print (" Neteisinga forma, loxe ")
