salle=[]
with open('test.txt','r',encoding='utf-8') as f:
    for elm in f.readlines():
        ligne=[]
        for i in elm[:-1]:
            ligne.append(i)
        salle.append(ligne)
print(salle)
def bouge(espace):
    for ligne in range(len(espace)):
        for place in range(len(espace[ligne])):
            if espace[ligne][place]!='.':
                pers=[]
                if (place==0 and ligne==0 )or  (place==0 and ligne==len(espace)-1 )or (place==len(espace[place])-1 and ligne==0) or (place==len(espace[place])-1 and ligne==len(espace)-1):
                    espace[ligne][place]='#'
                    print("ici",place,len(espace)-1)
                elif (ligne==0 or ligne==len(espace[ligne])-1) and place!=len(espace[ligne])-1:
                    print("la",ligne,place)
                    pers.append(espace[ligne][place+1])
                    pers.append(espace[ligne][place-1])
                    pers.append(espace[ligne+1][place-1])
                    pers.append(espace[ligne+1][place-1])
                    pers.append(espace[ligne+1][place+1])
                elif (place==0 or ligne==len(espace[ligne])-1) and place!=len(espace[ligne])-1:
                    print("la",ligne,place)
                    pers.append(espace[ligne+1][place])
                    pers.append(espace[ligne+1][place+1])
                    pers.append(espace[ligne][place+1])
                    pers.append(espace[ligne+1][place+1])
                    pers.append(espace[ligne+1][place+1])

                    
                elif ligne!=0 and ligne<len(espace[ligne])-1 and place!=len(espace)-1:
                    print("ouii")
                    for i in range(place-1,place+1):
                        pers.append(espace[ligne-1][place])
                        pers.append(espace[ligne+1][place])
                    pers.append(espace[ligne][place+1])
                    pers.append(espace[ligne][place-1])
                if pers.count('#')==0:
                    espace[ligne][place]='#'
                elif pers.count('#')>=4:
                    
                    espace[ligne][place]='L'
    return espace
            
            
def jeu():
    avant=salle
    apres=bouge(avant)
    print(apres)
jeu()
