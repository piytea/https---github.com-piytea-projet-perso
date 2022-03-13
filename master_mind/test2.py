import random


class Master:
    COLORS=[0,1,2,3,4,5]
    
    def __init__(self,trie=12,long=4,init="X"):
        """
        parametres de base d'une grille
        nbl et nbc : nb de ligne et de collonnes
        grilleInit: grille de nbl ligne et nbc col remplie avec init (= 0 par defaut)
        """
        self.nbl=trie
        self.nbc=long
        self.combi=[]
        self.grille=[[init]*self.nbc for x in range(self.nbl)]
        self.result=[[init]*self.nbc for x in range(self.nbl)]
        self.bon=0
        self.pasloin=0
        
    
    def combinaison(self):
        val=Master.COLORS
        print(val)
        
        for i in range(4):
            nb=val[random.randint(0,len(val)-1)]
            self.combi.append(nb)
            val.remove(nb)
        
    def nouvelprop(self):
        val=input("faites une proposition (0,1,2,3,4,5: ")
        return val
    
    def verif(self,prop):
        self.bon=0
        self.pasloin=0
        prop=(list(int(i) for i in prop ))
        for i in range(len(prop)):
            #print(self.combi[i],prop[i],prop)
            if int(prop[i])==self.combi[i]:
                self.bon+=1
            if prop.count(self.combi[i])>0 and int(prop[i])!=self.combi[i]:
                self.pasloin+=1
            
        return self.bon,self.pasloin
    def addresult(self,lg):
        i=0
        while i <4:
            
            for b in range(self.bon):
                self.result[lg][i]=2
                i+=1
                
            for pb in range(self.pasloin):
                self.result[lg][i]=1
                i+=1
                
            break

        print(self.result[lg])
    def __repr__(self):
        res=""
        
        for i in range(self.nbl):
            res+="\n"+str(i+1)+"\t|\t"+'\t'.join(str(val) for val in self.grille[i])+"\t|"+'  '.join(str(val) for val in self.result[i])+"|"

        return res
if __name__=="__main__":
    jeu=Master()
    jeu.combinaison()
    tour=0
    #print(jeu.combi)
    print(jeu)
    while jeu.bon!=4 and tour<12:
        jeu.grille[tour]=jeu.nouvelprop()
        bpbc,bc=jeu.verif(jeu.grille[tour])
        print("bien placés+ bonne couleur : ",bpbc,"\t juste bonne couleur : ",bc)
        jeu.addresult(tour)
        tour+=1
        print(jeu)
    if tour ==12 and jeu.bon!=4:
        print("vous avez perdu")
    else :
        print("bravo vous avez trouvé")

