nombre=[]
with open('input.txt','r',encoding='utf-8') as f:
    for ligne in f.readlines():
        nombre.append((int(ligne[:-1])))
def jeu():
    depart=0
    for i in range(25,len(nombre)):
        total=0
        prec=nombre[depart:depart+25]
        for nbi in prec:
            for nbj in prec:
                if nbi+nbj==nombre[i] and nbi!=nbj:
                    total+=1
        if total==0:
            return nombre[i],i
        depart+=1

                    
print(jeu())       

def jeu2():
    
    for i in range(667):
        total=0
        test=[]
        somme=0
        
        for nbj in range(i,667):
            somme+=nombre[nbj]
            test.append(nombre[nbj])
            if somme==2089807806 :
                return max(test),min(test),max(test)+min(test)
        
print(jeu2())
                    
        
    
   
