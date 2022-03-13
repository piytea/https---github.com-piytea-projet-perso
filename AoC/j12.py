valeurs=[]
with open('input.txt','r',encoding='utf-8') as f:
    for elm in f.readlines():
        valeur.append(elm)
print(valeur[:10])
        
