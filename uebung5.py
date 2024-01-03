#Uebungszettel 5
#Konzepte der Programmierung
#Tutor: Adrian-Maurice Alex
#Tutorium: Montag 12-14 Uhr 
#Von: Ibrahim Jarra , Lasse-Leander Kalweit, Florian Kremeier

import random
def ueb_b(xs,k):

   

    
    def suche(list1,k):

        if len(list1)==1:
            
            if list1[0]==k:
                if len(xs) ==1:
                    return "Es gibt kein größeres Element"
                return 1
            
            else:
                return "Element nicht in der Liste"
            
        elif len(list1)==0:
            return "Element ist nicht in der Liste"

        
        f= list1[len(list1)//2]

        if f> k:
            return suche(list1[:len(list1)//2:],k)
        
        elif f<k:
            return suche(list1[len(list1)//2::],k)
        
        elif f==k:

            for i in range(len(xs)):

                if xs[i]==k:
                    return i+1
            return False
        
    return suche(xs,k)

#print(ueb_b([1,2],2))

def ueb_c(xs,k):

    def suche(list1,k):

        if len(list1)==1:
            
            for i in range(len(xs)):
                if list1[0]==xs[i] and k==xs[i]:
                    return i+1
                
                elif list1[0]==xs[i] and k>=xs[i]:
                    return i+1
                elif list1[0]==xs[i] and k < xs[i]:
                    return i
                
            return 1
            
            
            
        elif len(list1)==0:
            return "Element ist nicht in der Liste"

        
        f= list1[len(list1)//2]

        if f> k:
            return suche(list1[:len(list1)//2:],k)
        
        elif f<k:
            return suche(list1[len(list1)//2::],k)
        
        elif f==k:

            for i in range(len(xs)):

                if xs[i]==k:
                    return i+1
            return False
        
    
    return suche(xs,k)
   
   
      
  
        


def insert(xs, i):
    key = xs[i]
    
    j=ueb_c(xs[:i:],key)
    
    xs.insert(j,key)
    for i in range(len(xs)):
        if xs[i]==key and i> j:
            #if i<len(xs)-1:
                
                #xs.remove(key)
            del xs[i] 
            break
            #else:
                #del xs[i]
                #xs.remove(xs[i])

                #break
    
def insertion_sort(xs):
    n = len(xs)
    # insert the elements step by step in the sorted front part
    for i in range(1,n):
        insert(xs, i)
    return xs
#print(insertion_sort([1,3,2,4,3,99,0]))
#print(insertion_sort([1,5,2,4,7,99,0,6,2]))
#print(ueb_c([1,5,2,4,7,99,0,6,2]))




    
    return xs
def ueb_e(xs):

    if len(xs) ==1:
        return xs
    help=int(len(xs)//(4/3))
    
    list_l=xs[:len(xs)//3:]
    list_m=xs[len(xs)//3:help:]
    list_r=xs[help::]

    
    return merge(insertion_sort(list_l),ueb_e(list_m),insertion_sort(list_r))
    
def merge(l,m,r):
    l_i=0
    m_i=0
    r_i=0
    sort=[]
    while(l_i<len(l)or m_i<len(m) or r_i < len(r)):
        if l_i<len(l)and m_i<len(m) and r_i < len(r):
            if l[l_i]<= m[m_i] and l[l_i] <= r[r_i]:
                sort.append(l[l_i])
                l_i +=1
            elif m[m_i] <=l[l_i] and m[m_i] <= r[r_i]:
                sort.append(m[m_i])
                m_i +=1
            elif r[r_i] <= l[l_i] and r[r_i] <=m[m_i]:
                sort.append(r[r_i])
                r_i +=1

        elif  l_i>=len(l)and m_i<len(m) and r_i < len(r):
            if m[m_i] <= r[r_i]:
                sort.append(m[m_i])
                m_i +=1
            else:
                sort.append(r[r_i])
                r_i +=1

        elif l_i<len(l)and m_i>len(m) and r_i < len(r):
            if l[l_i] <= r[r_i]:
                sort.append(l[l_i])
                l_i +=1
            else:
                sort.append(r[r_i])
                r_i +=1

        elif l_i<len(l)and m_i<len(m) and r_i > len(r):
            if l[l_i] <= m[m_i]:
                sort.append(l[l_i])
                l_i +=1
            else:
                sort.append(m[m_i])
                m_i +=1
        elif l_i<len(l):
            sort.append(l[l_i])
            l_i +=1
        elif m_i<len(m):
            sort.append(m[m_i])
            m_i+=1

        elif r_i <len(r):
            sort.append(r[r_i])
            r_i+=1
            
    return sort

print(ueb_e([1,9,2,3,6,5,122,4,8]))


def quick_sort(list1):
    pivot=0
    list_l=[]
    list_r=[]

    if len(list1) <=3:
        
        
        return list1
   
    else:
        pivot=(list1[0]+list1[1]+list1[2])//3

    for i in range(3,len(list1)):
        if list1[i] < pivot:
            list_l.append(list1[i])
        
        else:
            list_r.append(list1[i])

    return(quick_sort(list_l) +  quick_sort(list_r))
def ueb_2d(xs):

    if len(xs)<100:
        return selcetion_sort(xs)
    
    elif len(xs) >=100:
        return ueb_2d(quick_sort(xs))
    
def selcetion_sort(xs):
    small = 0
    i=0
    print()
    while(i<len(xs)):
        small=i
        for j in range(i,len(xs)):
            if xs[j] < xs[small]:
                small=j
         
       
        xs[i],xs[small]=xs[small],xs[i]
        i +=1
    return xs
def zufallsListe(n):
    xs = n * [0]
    for i in range(n):
        xs[i] = random.randint(0,n)
    
    return xs

#print(ueb_2d(zufallsListe(150)) )  

#print(selcetion_sort([3,4,7,8,99,0,1,3]))


#Aufgabe 2c

def partition2(xs, start, end):
    pivot = xs[start][0]
    l = start
    for i in range(start+1,end):
        if xs[i][0] < pivot:
            l = l+1
            xs[i], xs[l] = xs[l], xs[i]
    xs[start], xs[l] = xs[l], xs[start]
    return l


def quicksortneu(list):
    n = len(list)
    newlist = []
    newlist2 = []
    for i in range(n):
        newlist.append((list[i], i))

    def quicksort_help(start, end):
        if (end-start <=1):
            return
        split = partition2(newlist, start, end)
        quicksort_help(start, split)
        quicksort_help(split+1, end)
        
    quicksort_help(0, n)
    for i in range(n-1):
        if newlist[i][0] == newlist[i+1][0]:
            if newlist[i][1]>newlist[i+1][1]:
                a = newlist[i]
                newlist[i] = newlist[i+1]
                newlist[i+1] = a
                
    for i in range(n):
        newlist2.append(newlist[i][0])
    return newlist2
#print(quicksortneu([1,2,4,234,535,66,8,367,6,9,12,42,4,1]))

#Quelle lexikografische Ordnung von Tupeln: https://www.ruhr-uni-bochum.de/lmi/lehre/ds_ss18/res/fachverteilungssortieren.pdf