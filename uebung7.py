#Uebungszettel 7
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit




# summe(list[int]):int
#Vorrausetzungen: Liste besteht aus integer
#Effekt: -
#Result:Summe der geraden Zahlen in der Liste werden returned   
"""
print(summe([1,2,3,4,5,6,8])) =20
print(summe([]))=0
print(summe([1]))=0
"""

def summe(list1):

    # summe_help(list2[int], sum[int])
    # Vorraussetzung: Liste besteht aus Integer, sum ist ein Integer.
    # Effekt: /
    # Result: Die Funktion addiert gerade Zahlen aus der Liste zu der Variable sum hinzu. Anschließend returned sie sum.
    """
    return(summe_help(list2,sum)) = 20
    """

    # List und Integer werden als Parameter genommen.
    def summe_help(list2 : list,sum : int):
        
        # Wenn die Länge der liste 0 ist, dann wird sum returned.
        if len(list2)==0:
        
            return sum
        
        # Wenn der 0. Index der Liste gerade ist wird er zu sum addiert.
        if list2[0] %2==0:
            sum+=list2[0]

        # Die Liste wird um ein Element verkürzt, der Index 1 wird zum 0ten Index.   
        list2=list2[1::]
       
        # Die Liste und Sum wird returned.
        return(summe_help(list2,sum))

    return(summe_help(list1,0))  #Ruft die Funktion summe_help mit den Parametern list1 und 0 auf.

print(summe([1,2,3,4,5,6,8]))


