#Uebungszettel 6
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit, Florian Kremeier

"""
2a)


allgemeines Matrixsummenproblem: 
    Wenn eine quadratische Matrix nach dem Schema n*n existiert und die einzelnen Elemente der Matrix natürliche sein müssen existiert ein Wert, welche die Summe der einzelnen Elemente der Matrix wiederspiegelt.
    Input: n*n Matrix, wo jedes Element eine natürliche Zahl ist
    Output: Summe der einzelnen Elemente in der Matrix

spezielles Matrixsummenproblem:
    Wenn eine quadratische Matrix nach dem Schema n*n existiert und die einzelnen Elemente der Matrix natürliche sein müssen und die Spalten absteigend und Zeilen aufsteigend sortiert sind existiert ein Wert, welche die Summe der einzelnen Elemente der Matrix wiederspiegelt.
    Input: n*n Matrix, wo jedes Element eine natürliche Zahl ist und Zeilen aufsteigend und spalten absteigend sortiert sind
    Output: Summe der einzelnen Elemente in der Matrix

"""


#2b)
#matrix_summe(list[list[int]]) : int
#Precondition: Die Liste ist nicht leer, Die Matrix geht nach dem Schema n*n und die Elemente müssen natürliche Zahlen sein
#Effect: None
#Result: Die Summe der Elemente in der Matrix wird zurückgegeben
"""
Test Cases:
print(matrix_summe([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])) =64

print(matrix_summe([[1,2,3,4],[2,3,4,5]])) = 24

print(matrix_summe([[1,2,2,2],[1,2,2,2]])) =14
"""

def matrix_summe(xs):

    erg=0
    for x in range(len(xs)): #Geht durch jede Zeile der Matrix
        for i in range(len(xs[x])): #Geht durch jede Spalte der Matrix in der momentanen Zeile und addiert die jeweiligen Elemente  zu Erg
            erg+= xs[x][i]

    return erg #erg wird returned

print(matrix_summe([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]))

print(matrix_summe([[1,2,3,4],[2,3,4,5]]))

print(matrix_summe([[1,2,2,2],[1,2,2,2]]))



#Der Algorithmus löst auch das spezielle Matrixproblem. Es bleibt jedoch bei der Laufzeit O(n^2)



#ueb_2x[List[List[int]]] : int
#Precondition: Spalten absteigend sortiert, Zeile aufsteigend sortiert, eine n*n Matrix, nicht mehr als zwei verschiedene Elemente, Listen in Listen dürfen nicht leer sein. Außerdem müssen die elemente natürliche Zahlen seihen
#Effect: None
#Result: Die Summe der Elemente der Matrix wird zurückgegeben
"""
Test Cases:
print(ueb_2c([[1,2,2],[1,2,2],[1,1,1]])) =13
print(ueb_2c([[42]])) =42
print(ueb_2c([[1,2,2,2],[1,2,2,2],[1,1,1,1],[1,1,1,1]])) = 22


"""

def ueb_2c(xs):

    erg=0     
    n= xs[len(xs)-1][0]   #Zahl aus erster Spalte/unterste Zeile wird in n gespeichert
    m= xs[0][len(xs[0])-1] #Zahl aus letzter Spalte/erster Zeile wird in m gespeichert
    smallest=0
    if n==m:    #Wenn n gleich m ist wird die Anzahl der Elemente der Matrix addiert, erg zugewiesen und erg wird returned
        erg += len(xs)*len(xs[0])*n
        return erg
    
    if n<m:   #Wenn n<m ist, wird smallest der Wert n zugewiesen, wenn nicht der Wert m
        smallest=n
    else:
        smallest=m

    j=0
    i=0
    while j<len(xs) and i < len(xs[0]):  #Geht die Matrix durch. Wenn die kleinere Zahl beim Index ist, wird nach rechts gegangen. Wenn die Zahl die größere Zahl ist, wird nach unten gegangen.
        if xs[j][i] == smallest:
            erg += (len(xs)-j) *smallest  #Alle Einträge der momentanen Spalte, welche unter dem Element xs[j][i] liegen, werden zu erg addiert. Das element xs[j][i] auch
            i+=1

        elif xs[j][i] >smallest:  
            erg += (len(xs[0])-i) *xs[j][i] # Alle Einträge der momentanen Zeile, welche nach dem Element xs[j][i] liegen, werden zu Erg addiert. Das element xs[j][i] wird auch hinzu addiert.
            
            j +=1
    return erg


#Wegen der anderen Sortierung von dem allgemeinen Matrixsummenproblem, kann dieses nicht mit dem Algorithmus ueb_2c funktionieren.
      


    