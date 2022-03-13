passe=[]
ligne=[]
place=[]
with open('input.txt','r',encoding='utf-8') as f:
    for code in f.readlines():
        passe.append(list(code[:-1]))

for l in passe:
    ligne.append(l[:-3])
    place.append(l[7:])

def jeu():
    
    
    rang=127
    bas=0
    p=7
    b=0    
    for lettre in ["B","B","F","F","B","B","F"]:
        if lettre=="F":
            rang-=((rang-bas+1)/2)
            
        if lettre=="B":
            bas+=((rang-bas+1)/2)
            
    
    for n in ["R","L","L"]:
        for lettre in n:
            if lettre=="L":
                p-=((p-b+1)/2)
            if lettre=="R":
                b+=((p-b+1)/2)
    print(rang,p,rang*8+p)
        
                
                
jeu()
