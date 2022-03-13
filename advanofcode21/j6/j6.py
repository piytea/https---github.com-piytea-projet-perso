with open('inputJ6.txt', 'r') as fichier:
    txt = fichier.read()
txt=txt.split(",")
for x in range(len(txt)):
    txt[x]=int(txt[x])

test=[3,4,3,1,2]
dicoP={}

for i in range(9):
    dicoP[i]=txt.count(i)
    
def simulator(tmp,dicoP):
    for j in range (tmp):
        newdic={}
        for p in range(len(dicoP.keys())-1):
            newdic[p]=dicoP[p+1]
        newdic[6]+=dicoP[0]
        newdic[8]=dicoP[0]
        dicoP=newdic    
    return sum(dicoP.values())


print(simulator(80,dicoP))
print(simulator(256,dicoP))
