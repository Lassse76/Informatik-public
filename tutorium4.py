
"""
. Spiegelkodierung
Implementiert eine Funktion, die eine Zeichenkette bestehend nur aus Kleinbuchstaben erh¨alt und
jeden Buchstaben im Alphabet spiegelt.
Beispiel: spiegelcode("abcmn") ergibt "zyxnm"
2. Alternierende Quersumme
Implementiert eine Funktion, die eine nat¨urliche Zahl enth¨alt und ihre alternierende Quersumme
berechnet.
Beispiel: altQuersumme(1234) ergibt 2, denn 2 = +4 − 3 + 2 − 1.
3. Sortiert oder nicht sortiert – das ist hier die Frage
Implementiert eine rekursive Funktion, die ¨uberpr¨uft, ob eine Liste sortiert ist.
Bitte am Ende des Tutoriums ausf¨ullen, damit Max sich auf Mittwoch vorbereiten
kann: https://votingo.cedis.fu-berlin.de/A6CX06
Solltet ihr keine W¨unsche haben, tragt euch bitte trotzdem ein.

"""
def spiegelcode(wort):
    abc = {
        "a" : "z",
        "b" : "y",
        "c" : "x",
        "d" : "w",
        "e" : "v",
        "f" : "u",
        "g" : "t",
        "h" : "s",
        "i" : "r",
        "j" : "q",
        "k" : "p",
        "l" : "o",
        "m" : "n",
        "n" : "m",
        "o" : "l",
        "p" : "k",
        "q" : "j",
        "r" : "i",
        "s" : "h",
        "t" : "g",
        "u" : "f",
        "v" : "e",
        "w" : "d",
        "x" : "c",
        "y" : "b",
        "z" : "a"

    }
    wort = wort.lower()
    s = ''
    for x in wort:
        
        s += abc[x]
    return s

print(spiegelcode("Spiegel"))
print(spiegelcode("hkrvtvo"))

"""
def alt_quersumme(number):
    number = str(number)
    x_list = [i for i in number]
    #reversed(x_list)
    x_list = [i for i in reversed(x_list)]
    counter = 0
    """

            

def alt_quersumme(number,sum,k):

    if number==0:
        return number
    
    if k ==1:
        sum += number %10
        number=number //10
        return alt_quersumme(number,sum,-1)
    else:
        sum -= number %10
        number=number //10
        return alt_quersumme(number,sum,1)
    
    return 

    
    
            
print(alt_quersumme(1234,0,1))




