
#Uebungszettel 3
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit, Florian Kremeier

#foo(list[int],int) : Bool
#precondition: List is not empty, k is a Integer
#Effect: None
#Result: Return True if  k is bigger then every element in the list. When this is not the case, the function return False
'''''
test cases:
    foo(list[1,2,3],4) == true
    foo(list[1,2,3],0) == false 
    foo(list[1,2,3],"Haus") == error 
    foo(list["Haus",2,3],5) == error 
    foo[list[-1,3,4],3] ==true
'''''
def foo(xs, k):
    n = len(xs)   # length of the list is save in n
    for i in range(n):  # for loop for the length of the list xs
        xs[i] = (xs[i] <= k) #When the i element of the list is smaller then k, then the i element  get true. Otherwise it keeps the i element get false.
    erg = False  # The variable erg get the value False
    for b in xs: # The  programm iterate through the list xs
        erg = b or erg # The variable erg get the value of the element b if its true. Otherwise it keep erg
    return erg #erg gets returned
''''
Nebeneffekt: Die Werte der Liste werden durch neue Werte ersetzt. 
Warum ist das Unerwünscht: Eventuell möchte der Entwicker mit der originalen Liste weiterarbeiten. Es könnten weitere Fehler auftreten. 
'''''


# bar(list[int], int) : Integer or Bool
# Precondition: List not empty, k is integer.
# Effect: None
# Result: Returns the Bool erg as False if no element in list xs is smaller than k, otherwise returns True.

''' Test cases:
bar([1,2,3,2,1], 4) == True
bar([1,2,3,4], 5) == True
bar([4,3,2], 0) == False
bar([1,1,1,1] , 0) == False
bar([42]) == bar() missing 1 required positional argument: 'k'
bar([], 6) == No output.
'''
def bar(xs, k): # Funktion nimmt jeweils eine Liste und ein Integer.
    n = len(xs)
    erg = False
    for i in range(n): # In einem for loop with erg mit den Elementen von xs verglichen und eine Bool zugeordnet.
        erg = (xs[i] <= k) or erg
    return erg # Die Funktion returned einen Boolwert.
#print(bar([1,2,3,2,1], 4))
#print(bar([1,2,3,4], 5))
#print(bar([4,3,2], 0))
#print(bar([1,1,1,1,], 0))
#bar([42])
#bar([], 6)

# bar_recursive(list[int], int) : Integer or Bool
# Precondition: List not empty, k is integer.
# Effect: None
# Result: Returns the Bool erg as False if no element in list xs is smaller than k, otherwise returns True.

''' Test cases:
bar_recursive([1,2,3,2,1], 4) == True
bar_recursive([1,2,3,4], 5) == True
bar_recursive([4,3,2], 0) == False
bar_recursive([1,1,1,1] , 0) == False
bar_recursive([42]) == bar() missing 1 required positional argument: 'k'
bar_recursive([], 6) == No output.
'''
def bar_recursive(xs, k): # Rekursive Funktion nimmt jeweils eine Liste und ein Integer.
    n = len(xs)
    erg = False

    if len(xs) == 0: # Case der erg returned wenn die Liste leer ist.
        return(erg)
    

    if xs[n-1] <=k: # Letztes Element wird mit k ueberprueft und anschliessend wird erg ein Bool-Wert zugeordnet.
        erg=True
    else:
        erg=False
    bar_recursive(xs[:(n - 1)], k) # Rekursiver call von der Funktion.

#print(bar_recursive([1,2,3,2,1], 4))
#print(bar_recursive([1,2,3,4], 5))
#print(bar_recursive([4,3,2], 0))
#print(bar_recursive([1,1,1,1,], 0))
#bar_recursive([42])
#bar_recursive([], 6)
    


# Aufgabe 1c
# add(list[int],list[int])  : list[int], int
# Precondition: List 1 and List 2 not empty. 
# Effect: Prints the sum.
# Result: kompartmentwise added list is returned. dot product of both lists printed
'''Test cases:
add([], []) == [], 0
add([1, 2, 3], []) == [1, 2, 3], 0
add([], [1, 2, 3]) == [1, 2, 3], 0
add([1], [1]) == [2], 1
add([1,2], [1]) == [2, 2], 3
add([1, 2, 3, 4], [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 5], 35
'''

def add(a : list,b : list):
    try:
        list = []  # anlegen einer leeren liste
        ma = max(len(a), len(b)) # die Länge der längeren der beiden Listen wird ermittelt
        
        for i in range(0,ma): 
            
            list.append(a[i]+b[i]) # der liste wird die Summe der Eingabe-Listen pro index hinzugefügt
        
        list2 = [] # anlegen einer weiteren leeren liste
        sum=0 # die Summe ist anfangs 0
        mi = min(len(a), len(b)) # die Länge der kurzeren der beiden Listen wird ermittelt
        for x in range(mi):
            list2.append(a[x]*b[x]) # das Produkt der Werte der Eingabe-Listen pro index wird der Liste hinzugefügt
        for i in range(len(list2)):
            sum +=list2[i] # Die Werte der Liste werden summiert
        print(sum) # Das Skalarprodukt der Eingabe-Listen wird auf dem Bildschirm ausgegeben
        return(list) # Die kompartmentweise Summierte liste wird zurückgegeben
    except:
        print("Eingaben keine Liste.") # Wenn mindestens eine der Eingaben keine Liste war, kann die Funktion nicht ausgeführt werden.
    
#print(add([1,1,2,1,1], [1,1,1,1,1]))

# recursive_function([int], int) : void
# Precondition: Both numbers are integers.
# Effect: Prints the Nachkommazahl.
# Result: Calculates and prints the Nachkommazahl.
'''Test cases:
recursive_function(0.1, 0) = 1
recursive_function(0,01, 0) = 2
recursive_function(0.589, 0) = 3
recursive_function(0,1, 1) = 2'''

def recursive_function(num, count ):
    #if isinstance(num, int) == True:
    if num %10 ==0.0 or num %10 ==1.0 or num %10 ==2.0 or num %10 ==3.0 or num %10 ==4.0 or num %10 ==5.0 or num %10 ==6.0 or num %10 ==7.0 or num %10 ==8.0 or num %10 ==9.0: 
        print(count) # Ausgabe der Anzahl von Nachkommastellen auf dem Bildschirm
        quit()
    else:
        count += 1 # Anzahl der Nachkommastellen wird um 1 erhöht
        recursive_function(num *10, count) # Die Funktion wird rekursiv aufgerufen, indem das zehnfache der ursprungszahl verwendet wird 
    

#print(recursive_function(0.003,0))

# dna2rna([list) : void
# Precondition: Input is a list.
# Effect: Prints the RNA-String. Keeps the original DNA-String.
# Result: This functions changes a DNA-String into a RNA-String and retuns void.
'''Test cases:
dna2rns(['T', 'A', 'C']) = ['U', 'A', 'C']
dna2rns([]) = []'''

def dna2rna(dna : list):
    list1=[] # Erzeugung einer leeren Liste
    for i in range (len(dna)): # Schleife, die für jedes Element in der Eingabeliste einmal ausgeführt wird
        
        if dna[i] == 'T': 
            list1.append('U') # Für ein jedes T wird ein U in die neue Liste hinzugefügt
        else:
            list1.append(dna[i]) # Alle Werte in der Eingabeliste, die nicht T sind werden der neuen Liste hinzugefügt

    print(list1)
dna2rna(['A','T','G','C','T','A','C','G'])



# dna2rna([list) : void
# Precondition: Input is a list.
# Effect: Prints the RNA-String. Modifies the DNA-String.
# Result: This functions changes a DNA-String into a RNA-String and returns void.
'''Test cases:
dna2rns2(['T', 'A', 'C']) = ['U', 'A', 'C']
dna2rns2([]) = []'''

def dna2rna2(dna : list):
    for i in range (len(dna)): # Schleife, die für jedes Element in der Eingabeliste einmal ausgeführt wird
        if dna[i] == 'T':
            dna[i] = 'U' # EIn jedes T wird durch ein U ersetzt

    print(dna)
#dna2rna2(['A','T','G','C','T','A','C','G'])

'''''
 Verhalten: -Ursprüngliche Liste wird bei dna2rna nicht verändert

Vorteile von dna2rna gegenüber dna2rna2: -Man kann mit Ursprünglicher Liste weiterarbeiten 

Nachteile on dna2rna gegenüber dna2rna2: -weniger Speicherplatz benötigt
                                         


'''''
#k_smallest(list[int(float)], int,float) : void
#Preconditions: The list and klein_k contains only integers and floats. Also klein_k must be bigger then the numbers in the list. 
#Effect: print the smallest number in the list
#Result: Return nothing
'''Test cases:
k_smallest([12, 4, 56, 0.9, 0.345], 100) = 0.345
k_smallest([1], 100) = 1
'''
def k_smallest(list1,klein_k):
    n = len(list1) # Der Länge der Eingabeliste wird eine Variable zugeordnet

    
    if n == 0:
        print(klein_k) # Sollte die Eingabeliste eine Länge von 0 haben, wird der eingegebene Wert ausgegeben
        quit() # Die Funktion wird verlassen solbald n = 0 ist
    elif n == 1:
        element = list1.pop() # Sollte die Länge der Liste genau 1 sein wird dem einen Element in der Liste die Variable element zugeordnet, außerdem wird der Wert aus der Liste gelöscht

        if element < klein_k:
            klein_k=element # Sollte element kleiner sein als klein_k wird klein_k auf den Wert von element gesetzt

    else:        
        element = list1.pop() # Hat die Eingabeliste mehr als ein Element wird dem ersten Wert in der Liste die Variable element zugeordnet, außerdem wird der Wert aus der Liste gelöscht
        element2 = list1.pop() # Gleichfalls wird dem zweiten Element die Variable element2 zugeordnet, außerdem wird der Wert aus der Liste gelöscht
        if element < element2:
            klein_k = element # Wenn element kleiner ist als element2 wird klein_k auf dem Wert von element gesetzt
        else:
            klein_k = element2 # Ist element nicht kleiner als element2 wird klein_k auf den Wert von element2 gesetzt
        
        
    k_smallest(list1,klein_k) # Die Funktion wird rekursiv aufgerufen

k_smallest([1.3],4)

#quersumme(int,int) : void
#Preconditions: Both numbers are integer
#Effect: print the Quersumme
#Result: Return nothing
'''Test cases:
quersumme(10, 0) = 1
quersumme(324, 0) = 9
quersumme(214, 5) = 12'''

def quersumme(zahl,summe):
    
    if zahl//10 ==0:  #Ganzzahliges teilen durch 10, wenn es 0 ergibt, wird die summe um die zahl modulo 10 erhöht. Die Rekursion hört auf. Dies ist der Rekursionsanker
        summe += zahl%10 
        print(summe) #Summe wird geprintet
        return 
  
    summe += zahl%10  #Zahl wird modulo 10 gerechnet, um die einzelnen Ziffern der Zahl zu bekommen. Z.B.: 15%10 = 5 . Das Ergebnis wird dann zur variable summe addiert
    quersumme(zahl//10,summe)   #Die Funktion Quersumme ruft sich selbst nochmal auf(rekursion), jedoch bei der variable Zahl ohne die Ziffer ganz rechts. Die Summe wird auch übergeben 
#quersumme(15,0)

quersumme(5949494,0)
quersumme(123,0)
quersumme(1111111111,0)