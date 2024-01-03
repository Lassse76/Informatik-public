import random
import math
import sys
#Uebungszettel 2
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit, Florian Kremeier
'''
Uebung 1a)
s
1b)=Datentypen
1c)=Datentypen, Imperative Grundlagen, Suchen und Sortieren
1d)=Datentypen,  Suchen und Sortieren
2a)=Funktionen,Datentypen
2b)=Funktionen, Suchen und Sortieren
2c)= Suchen und Sortieren
2d)=Funktionen




Uebung 1b)

Probleme mit Integer:

-da in Python jede beliebige natürliche Zahl ein Integer sein kann, kann die Laufzeit deutlich langsamer werden(ist ineffektiv)(hängt mit der Implementation zusammen). (Problem in Python)
-Ein Overflow kann entstehen, wenn man einer natürliche Zahl einen Datentypen zuweist, diese natürliche Zahl jedoch nicht im Wertebereich des Datentypes liegt. (Nicht in Python)

-bei 4 Bit  können Zahlen zwischen -8 bis 7
    0111
   +0001
   ------
    1000 <----  Overflow denn die Grenzen reichen nicht aus um die Zahl zu errechnen. In dem Fall wäre 7+1 =-8.

Probleme mit Floats &Doubles:
-unendlich viele Floats können nicht in Programmiersprachen representiert werden, da floating und doubles nur bestimmt groß bzw. klein sein dürfen(Problem in Python und anderen Programmiersprachen)
-Rundungsfehler können auftreten(Da Gleitkommazahlen in Bits gespeichert werden)(Python und andere Programmiersprach)
-mathematische Gesetze funktionieren teilweise nicht(Python und andere Programmiersprachen)
'''

 
def float_proof():
    print(0.9899432893243809343098329432879348924379823) #Bei der Ausgabe werden nach ca. 30 Nachkommastellen die restlichen Zahlen nicht mehr ausgegeben. Das ist ein Beweis das unendlich viele Nachkommastellen nicht angegeben werden könne.
float_proof()

def rundung_proof():
    kleine_zahl = 0.0000000000000000000000000000000001  #Beweis von Rundungsfehler
    print(1+kleine_zahl)
rundung_proof()

def assoziativ_proof():  #Beweis das nicht alle mathematische Gesetze bei floats funktionieren(in dem Fall Assoziativität)
    print((0.0000000000023*0.000003)*0.000003)
    print((0.000003*0.000003)*0.0000000000023)
assoziativ_proof()


def uebung1bint() :
    num=0
    for i in range(math.factorial(1000000000)): #Nachweis der langen Laufzeit bei sehr großen Integer
        num = 1+math.factorial(1000000000)    

   

#uebung1bint()

def uebung1c():

    word = input("Gib was an:")

       

    output = {}
    for i in range(len(word)):  #itteriert duruch den String. 
        #if i in listkey:
            if word[i] not in output: #Wenn das Zeichen nicht im Dictionary existiert, wird es hinzugefügt.
                output[word[i]]  = 1
            else:  #Wenn das Zeichen schon im Dictionary existiert, wird der Wert um 1 erhöht.
                output[word[i]] += 1
    print(output)
#uebung1c()

def uebung1d():
    reversed = [] # Leere Liste um den DNA-String unmzukehren.
    kompl = [] # Liste für Komplimentären String.
    dna = input("DNA Sequenz:") # Input von User.
    for base in range(len(dna)-1, 0, -1): # Loop durch den DNA-String, Ende und Anfang vertauscht, Iterator läuft rückwaärts.
        reversed.append(dna[base]) # DNA-String rückwärts in Liste einfügen.
    for base in range(len(reversed)): # If else Statement um jeweiligen Character zu überprüfen und die komplimentäre Base in die kompl. Liste einfügen.
        if reversed[base] == 'A':
            kompl.append('T')
        if reversed[base] == 'T':
            kompl.append('A')
        if reversed[base] == 'C':
            kompl.append('G')
        if reversed[base] == 'G':
            kompl.append('C')
    print(dna) # DNA-String 
    print(reversed)
    print(kompl)
#uebung1d()



def uebung2a(): # Zufälligen DNA-String erzeugen mithilfe des Random Modul.
    base = ['A','T','C','G']
    
    dna = [random.choice(base) for i in range(6)] 
   
    
    return dna

#print(uebung2a())    

def uebung2b(dna1, dna2): #Überpfrüfung ob zwei dna Strings gleiche Zeichen haben
    same=[] #gleiche Zeichen werden hier drin gespeicher
    for i in range(6): #DNA strings werden durch itteriert
        if dna1[i] == dna2[i]: #Überprüfung, ob Zeichen i des dna-stings gleich ist
            same.append(i)# Zeichen wird der Liste "same" hinzugefügt
    return(len(same))# Länge der Liste wird wiedergegeben, um die Menge der gleichen Zeichen widerzugeben



def uebung2c(dna1, dna2): # Überprüfung ob 2 DNA-Strings die gleiche Anzahl von Basen am gleichen Platz besitzen.
    dna1_basen = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0} # Counter pro Base.
    dna2_basen = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0} # Counter pro Base.
    samestuff =0
    for i in range(6): # DNA Basen und ihre Position werden gezählt und dem Dictionary hinzugefügt.
         
        dna1_basen[dna1[i]] +=1
        dna2_basen[dna2[i]] +=1


    # Wenn die Basen an der gleichen Position die gleiche Anzahl besitzen wird die Variable samestuff um 1 erhöht.
    if dna1_basen.get('A') == dna2_basen.get('A'):
        samestuff +=1
    if dna1_basen.get('T') == dna2_basen.get('T'): 
        samestuff +=1 

    if dna1_basen.get('C') == dna2_basen.get('C'): 
        samestuff +=1 

    if dna1_basen.get('G') == dna2_basen.get('G'): 
        samestuff +=1

    
    return(samestuff) # Samestuff wird returned.
    
    
def uebung2d():
        ca=["B","D","E","F","H","i","J","K","L","M","N","O","P""Q","R","S","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"] #Liste mit Zeichen, welche nicht im DNA-String vorkommen dürfen
        dna2=""
        dna1_list= uebung2a()
        dna2_list=[]
        test=0
        while True:
            try:
                dna2=input("6stellige DNA:") # DNA-String 2 muss vom User eingegeben werden
                dna2 = dna2.upper() #Kleinbuchstaben werden in Grßbuchstaben umgewandelt (dadurch werden Fehler durch groß und Kleinschreibung vermieden)
                
                    
                    
                            
                
                for i in range(6):  #Itteration durh DNA2-string
                    
                    dna2_list.append(dna2[i])   #Der Liste werden die einzelnen Elemente des DNA2-Strings gegeben(Nötig um andere Funktionen zu nutzen)

                sameposition = uebung2b(dna1_list, dna2_list) #Funktion uebung2b wird mit den Listen "dna1_list" und "dna2_list" aufgerufen
                if sameposition==6:
                    print("Richtig erraten")
                    quit()

                # Dem User wird die Anzahl der richtigen Positionen angezeigt.
                else:
                    for letter in range(len(dna2_list)):
                        if dna2_list[letter] in ca: #Falls Zeichen welche nicht in DNA-String vorkommen dürfen vorkommen, wird das Programm gequittet. Dieser Vergleich ist nötig, um unnötige Terminalausgaben zu verhindern.
                            
                            quit()
                    print(f" {sameposition} war richtig" )

                sameamount = uebung2c(dna1_list,dna2_list) # Funktion Uebung2c wird aufgerufen.
                print(f"{sameamount} haben die gleiche Anzahl")
                dna2_list =[]
                dna2=""
                test=0
                correct=False
            except: 
                print("Falsche Eingabe")
                quit() # Bei einem Fehler wird das Programm beeendet.
                

  

#uebung2d()
#uebung2c(uebung2a(),uebung2a())
#uebung1c()
            




