valeurs=[]
with open('input.txt','r',encoding='utf-8') as f:
    for elm in f.readlines():
        valeurs.append(elm[:-1])
print(valeurs[:10])
print(valeurs[1][1:])
