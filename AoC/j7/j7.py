couleurs=[]
with open('input.txt','r',encoding='utf-8') as f:
    for valise in f.readlines():
        couleurs.append(valise.split(" ")[:-1])


newlist=[]
cle=[]
val=[]

mot=["bags","bag","bag,","bags,","bags./n","bag./n","contain"]
for i in range(len(couleurs)):
    vrai=[]
    li=[]
    if "no" not in couleurs[i]:
        
        for elm in couleurs[i]:
            if elm not in mot and len(elm)>1:
                li.append(elm)
    
    
    for i in range(0,len(li),2):
        vrai.append(li[i]+" "+li[i+1])
    if len(vrai)>1:
        newlist.append(vrai)

for l in newlist:
    
    cle.append(l[0])
    val.append(l[1:])


dico_couleurs=dict(zip(cle,val))



def direct(liste):
    sac=0
    
    if "shiny gold" in liste:
        sac+=1
            
    return(sac)


def main(valise):
    sac=0
    for val in valise[1] :
        if dico_couleurs.get(val):
            sac+=direct(dico_couleurs.get(val))
            print(val,dico_couleurs.get(val))
            main(dico_couleurs.get(val))
            print(sac)


    return(sac)

for i in dico_couleurs.items():
    
    print(i)
    total=0
    total+=main(i)
    


    
    

