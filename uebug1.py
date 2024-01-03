#Uebungszettel 1
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit, Florian Kremeier

def uebung1a(a, h):
    print((a * h) / 2)
def uebung1b(i):
    if i==1:
        pass
    elif i==2:
        pass
    elif i==3:
        pass
    #...


def uebung1c(anfang,ende,schritt): 
    '''
    Funktion nimmt 3 Parameter, 
    die den Anfang, das Ende und den Schritt des For-Schleife darstellen.
    '''
    while anfang<ende: # Überprüfung, ob die Zählervariable unter der Endvariable liegt
        print(anfang) #Zählervariable wir ausgegeben
        anfang+=schritt # Zählervariable wird schrittweise erhöht.
        

#uebung1c(1,4,2)


def vergleich(num1, num2):
    return(num1 != num2)

def ueb1d(num1, num2, num3):
    test1 = vergleich(num1,num2)
    test2 = vergleich(num1,num3)
    test3 = vergleich(num2,num3)
    print(test1 and test2 and test3 == True)

def uebung1e():
    i=int
    summe_eingabe=0
    zähler=-1
    while i != 0:
        
        i=int(input())
        zähler +=1
        summe_eingabe+=i
    if zähler != 0:
        print(summe_eingabe/zähler)
    else:
        print("0")

#uebung1e()
#ueb1d(1,1,4)

def uebung2a():
    age = int
    if age < 12:
        print("Preis: 10 Euro")
    elif age < 18 or age > 65:
        print("Preis: 12 Euro")
    else:
        print("Preis: 14 Euro")

uebung2a()

def uebung2b():
    age = int
    custom_else = False
    if age < 12: # If Bendingung mit Exit.
        print("Preis: 10 Euro")
        exit()
    if age < 18 or age > 65: # If Bedingung mit Exit.
        print("Preis: 12 Euro")
        custom_else = True
        exit()    
    if custom_else == True: # Optionale Bedingung für das else-Statement
        print("Preis: 14 Euro")




def uebung2c():
    #Die Do-while Schleife führt erstmal den Inhalt der Schleife aus, bevor sie die Bedingung übeprüft.
    i=0
    while():
        a = (i+1)
        i+=1
        if a == 2:
            break
        


def vergleich2(same):
    print(same)

def uebung2d(number1,number2,number3):
    
    same=0
    if number1==number2 and number1==number3:
        vergleich2(0)
        exit()
    elif number1!=number2 and number3==number2:
        vergleich2(1)
        exit()
    elif number1!=number3 and number2==number1:
        vergleich2(1)
        exit()
    
    elif number2!=number3 and number1==number3:
        vergleich2(1)
        exit()
    same=3
    print(same)

#uebung2d(3,3,3)

def pyramide():
    list2 = ["     1     ","    212    ","   32123   ","  4321234  "," 543212345 ","65432123456"]
    for i in range(0,6):
        print(list2[i])

#pyramide()