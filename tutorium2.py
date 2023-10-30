import random
def uebung2():

    dezimal = int(input("Gib eine Zahl an: "))
    rest=[]
    binär=""


    while dezimal !=0:
        rest.append(dezimal %2)
        dezimal= dezimal//2

    i= len(rest)-1
    rest = rest[::-1]
    """while len(rest) !=0:
        binär = binär + str(rest[i])
        rest.pop()
        i -=1
    """
    print(binär)
    print(rest)

#uebung2()

def uebung3():
    liste = {
            "Schoko":0,
            "Erdbeere" : 0,
            "Vanille" : 0,
            "Oreo":0,
            "Zitrone":0,
        }
    while True:
        bestellung= input("Was willste?")
        
        
        

        match bestellung:
            case "Schoko" :
                liste["Schoko"] += 1
            case "Erdbeere":
                liste["Erdbeere"] += 1
            case "Vanille":
                liste["Vanille"] += 1
            case "Oreo":
                liste["Oreo"] += 1
            case "Zitrone":
                liste["Zitrone"] += 1
            case "beenden":
                print(liste)
                quit()
#uebung3()

def rndmlst():
    zahlenliste = []
    for i in range (0,41):
        zahl = random.randint(0,200)
        zahlenliste.append(zahl)
        zahlenliste.append("bliblablub")
        zahlenliste.append(zahl+0.42)
    return(zahlenliste)
def uebung4():
    liste= rndmlst()
    gerade=[]
    ungerade=[]

    # a[0:len(liste):3]
    a = liste[0:len(liste)-1:3]
    #a = slice(0,len(liste)-1,3)

    for i in range(len(liste) // 3):
        print(a)
        

        if a[i] % 2 ==0:
            gerade.append(a[i])
        else:
            ungerade.append(a[i])

    print(f" Die Listen: Ungerade: {ungerade} Gerade: {gerade}")

uebung4()