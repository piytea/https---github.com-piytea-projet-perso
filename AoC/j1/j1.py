lprix=[]

with open('input.txt','r',encoding='utf-8') as f:
    for prix in f.readlines():
        lprix.append(int(prix))


print(lprix)
def jeu():
    somme=0
    for i in range(len(lprix)):
        for n in range(i,len(lprix)):
            for l in range(n,len(lprix)):
                if lprix[i]+lprix[n]+lprix[l]==2020:
                    somme=lprix[i]*lprix[n]*lprix[l]
                    return somme,lprix[i],lprix[n],lprix[l]
print(jeu())
