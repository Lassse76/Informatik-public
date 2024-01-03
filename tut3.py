import math
adult = False

def init_adult():
    if int(input("Alter: ")) >= 18:
        adult = True

def check_adult():
    if adult:
        print("Du bist volljährig.")
    else:
        print("Du bist minderjährig.")

def palindrom(zahl1 : int):

    zahl1=zahl1

    zahlstr= str(zahl1)

    n= len(zahlstr)
    if n %2==0:
        zahl_l = zahlstr[:n//2]
        zahl_r = zahlstr[n//2:]
    else:
        zahl_l = zahlstr[:n//2]
        zahl_r = zahlstr[n//2+1:]

    
    print(zahl_r[::-1] == zahl_l)

    
        

    
    print(zahl_l,zahl_r)
    pass


def recursionen(a,n):

    if n==1:
        
        return(a)
    
    return(a*recursionen(a,n-1))
    
    
#init_adult()
#check_adult()
#palindrom(12322)
print(recursionen(3,3))


# min_liste(list[list[int]]) : None
# Voraussetzung: l ist nicht leer und jede Liste in l enthält mindestens ein Element.
# Effekt: Jedes Listen-Element in l wird durch sein jeweiliges Minimum ersetzt.
# Ergebnis: None
''' Testfälle:
liste1 = [[76, 100, 50], [24], [120, 60, 29, 45], [50, 70]]
liste2 = [[30, 98, 35, 60], [102, 120, 40], [50]]
liste3 = [[20, 150], [200, 19]]
min_liste(liste1) 
min_liste(liste2) 
min_liste(liste3) 
liste1 == [50, 24, 29, 50]
liste2 == [30, 40, 50]
liste3 == [20, 19]
'''
def min_liste(l: list):
    # TODO: Methode impleren
    
    for i in range(len(l)):
        min


# max_von_mins(list[list[int]]) : int
# Voraussetzung: l ist nicht leer und jede Liste in l enthält mindestens ein Element.
# Effekt: None
# Ergebnis: Das Maximum der Minima von den jeweiligen Listen-Elementen in l wird zurück gegeben.
''' Testfälle:
max_von_mins([[76, 100, 50], [30, 70]]) == 50
max_von_mins([[76, 100, 30], [30, 70]]) == 30
max_von_mins([[123, 250, 164, 31], [60, 65], [37, 260]]) == 60
'''
def max_von_mins(l):
    # TODO: Funktion implementieren
    ...
