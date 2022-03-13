collone=[]
tableau=[]
with open('input.txt','r',encoding='utf-8') as f:
    for code in f.readlines():
        collone.append(list(code[:-1]))

for i in range(100):
    tableau.append(collone)
def jeu(a,b):
    y=0
    x=0
    z=0
    arbre=0
    print(len(collone[0]),len(collone))
    while y!=(len(collone)-1):
        x+=a
        y+=b
        
        if x>=len(collone[0])-1:
            z+=1
            x=x-len(collone[0])
        if tableau[z][y][x] == '#':
            arbre=arbre+1
    return x,y,arbre
    

              
def total():
    print(jeu(1,1),1,1)
    print(jeu(3,1),3,1)
    print(jeu(5,1),5,1)
    print(jeu(7,1),7,1)
    print(jeu(1,2),1,2)
    
print (total())
print(60*286*76*62*45)
