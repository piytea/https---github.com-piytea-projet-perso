passe=[]

with open('input.txt','r',encoding='utf-8') as f:
    for code in f.readlines():
        passe.append(list(code[:-1]))
liste=[]
for i in range(128):
    for y in range (8):
        
        liste.append(i*8+y)

def jeu():
    nombre=[]
    maplace=[]
    for ligne in passe:
        rang=127
        bas=0
        p=7
        b=0
        for i in ligne[:-3]:
            
            
            
            for lettre in i:
                if lettre=="F":
                    rang-=((rang-bas+1)/2)
                if lettre=="B":
                    bas+=((rang-bas+1)/2)   

        for n in ligne[7:]:
            
            for lettre in n:
                if lettre=="L":
                    p-=((p-b+1)/2)
                if lettre=="R":
                    b+=((p-b+1)/2)
                    
        nombre.append(int(rang*8+p))
    for i in liste:
        if i not in nombre:
            maplace.append(i)
    
    print(max(nombre),maplace)
                
jeu()
