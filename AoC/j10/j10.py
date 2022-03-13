entree=[0]
with open('input.txt','r',encoding='utf-8') as f:
    for ligne in f.readlines():
        entree.append((int(ligne)))

nombre=sorted(entree)

def jeu():
    jun=0
    jdx=0
    jts=1
    for i in range(len(nombre)-1):
        if nombre[i+1]-nombre[i]==1:
            jun+=1
        elif nombre[i+1]-nombre[i]==2:
            jdx+=1
        elif nombre[i+1]-nombre[i]==3:
            jts+=1
    return jun,jdx,jts,jun*jts

dernier=max(nombre)

def explore(d,l,nb):
    if d==dernier:
        nb+=1
        if nb%1000000==0:
            print(nb/1e12)
        return nb
    for v in l:
        if v-d>3:
            break
        elif v-d>0:
            nliste=l.copy()
            nliste.remove(v)
            #print("explore",v,nliste)
            nb=explore(v,nliste,nb)
    return nb

fait={}
for i in nombre:
    fait[i]=0
print(fait)


def explore2(i,an,nb):
    if nombre[i]==dernier:
        nb+=1
    #    print("chemin",nombre[i])
        return nb
    #print("ici",nombre[i],nombre[an],nb)
    
    for v in range(i,len(nombre)):
        if nombre[v]-nombre[i]>3:
            break
        elif nombre[v]-nombre[i]>0:
            print("explore",nombre[v],nombre[i])
            nb=explore2(v,i,nb)
    fait[nombre[i]]+=1
    print(fait,v,an)        
    return nb        
            
def explore3(i):
    if nombre[i]==dernier:
        return 1
    nb=0
    for v in range(i,len(nombre)):        
        if nombre[v]-nombre[i]>3:
            break
        elif nombre[v]-nombre[i]>0:
            if (fait[nombre[v]])==0:
                fait[nombre[v]] = explore3(v)
            nb += fait[nombre[v]]
    return nb        

nb=explore3(0)
print(nb)
