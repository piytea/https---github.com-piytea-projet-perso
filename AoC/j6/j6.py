passager=[]
pers=[]
nb=0
lettres=list(map(chr, range(97, 123)))
with open('input.txt','r',encoding='utf-8') as f:
    for q in f.readlines():
        
        pers+=(list(q[:-1]))
        if len(q)<=1:
            nb+=1
            passager.append(pers)
            pers=[]
print(passager[10])

print(len(lettres))
def jeu():
    ouii=0
    tust=0

    for fam in passager:
        tust+=1
        ouin=0
        for l in lettres:
            if fam.count(l)>=1:
                ouin+=1

        
        ouii+=ouin
            
    return ouii,tust

print(jeu(),nb)
        
