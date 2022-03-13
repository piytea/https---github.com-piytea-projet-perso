import random
#generation de la grille
class Grille:
    DIR={"N": [0,-2], "S": [0,2], "E": [2,0], "O": [-2,0]}
    
    def __init__(self,nbl,nbc,init=0):
        """
        parametres de base d'une grille
        nbl et nbc : nb de ligne et de collonnes
        grilleInit: grille de nbl ligne et nbc col remplie avec init (= 0 par defaut)
        """
        self.nbl=nbl
        self.nbc=nbc
        self.grilleInit=[[init]*self.nbc for _ in range(self.nbl)]
    
    
    def dir(self):
        # donne une liste de 4 direction choisi aleatoirement dans DIR
        a=list(Grille.DIR.values())
        random.shuffle(a)
        return(a)
    
    def rotation90(self,direc):
        #tourne la grille à 90 ° à gauche ou droite en fonction de "direc"
        
        bl,bc,ol,oc=2,2,2,2
        gr=[[0]*self.nbc for _ in range(self.nbl)]
        
        for i in range(self.nbl):
            for y in range(self.nbc):
                if direc=="g":
                    gr[self.nbl-y-1][i]=self.grille[i][y]
                    if self.grille[i][y]=="B":
                        bl,bc=self.nbl-y-1,i
                    if self.grille[i][y]=="O":
                        ol,oc=self.nbl-y-1,i
                if direc=="d":
                    gr[y][self.nbl-i-1]=self.grille[i][y]
                    if self.grille[i][y]=="B":
                        bl,bc=y,self.nbl-i-1
                    if self.grille[i][y]=="O":
                        ol,oc=y,self.nbl-i-1
        self.grille=gr
        return bl,bc,ol,oc

        
        
    def __repr__(self):
        res=""
        for ligne in self.grille:
            res+="\n|\t"+'\t'.join(str(val) for val in ligne)+"\t|"
        return res


class Laby(Grille):
    """
    fonctions concernant la gestion des fonctionalités du laby en alphanum
    herite de Grille
    self.grille == (un quadrillage #/P)
    nb ligne et nb collone est tjrs impaire
    bl et bc corespondent a la pos de la bille (2,2 au depart)
    p pour les murs
    X pour la bordure
    # pour les cases
    """
    def __init__(self,nbl,nbc,bl=2,bc=1):
        
        if nbl%2==0:
            nbl+=1
        if nbc%2==0:
            nbc+=1
            
        Grille.__init__(self,nbl,nbc,"#")
        self.grille=self.grilleLaby()
        self.nbl=nbl
        self.nbc=nbc
        self.bl=bl
        self.bc=bc
        self.ol=0
        self.oc=0
        self.recupO=0
        self.mouvBall=[]
        
    def grilleLaby(self):
        # modifie la grille pour obtenir un quadrillage P/#
         
        for i in range(self.nbl):
            for n in range(self.nbc):
                if n==0 or i==0 or i==self.nbl-1 or n==self.nbc-1:
                    self.grilleInit[i][n]="X"
                elif n%2 ==0 and i%2 ==0:
                    self.grilleInit[i][n]="#"
                else:
                    self.grilleInit[i][n]="p"
        return self.grilleInit

    def chemin(self,x,y):
        """
        algorithme de generation du laby
        part le la pos (x,y)
        """
        self.grille[y][x]=" "
        direction=self.dir()
        for i in direction:
            a,b=i[0],i[1]
            nx,ny= x+a, y+b
            if (nx<len(self.grille[0]) and ny<len(self.grille[0])) and (self.grille[ny][nx]=="#"):
                self.grille[int(y+(ny-y)/2)][int(x+(nx-x)/2)]=" "
                self.chemin(nx,ny)
                
    def entresors(self):
        # indique l'entrée (E en haut a gauche) et la sortie ( S en bas a droite) dans la grille
        self.grille[2][2]="E"
        self.grille[self.nbl-3][self.nbc-2]="S"
    
                
    def rotation90(self,direc):
        # updte de rotation90 pour obtenir les coordonées de la bille apres une rota90
        print(self.bc,self.bl)
        self.bl,self.bc,self.ol,self.oc=Grille.rotation90(self,direc)
        print(self.bc,self.bl)
        self.bille()
        
    def gravite(self):
        # fait tomber la balle verticalement
        
        self.grille[self.bl][self.bc]=" "
        while (self.grille[self.bl+1][self.bc]==" ") or (self.grille[self.bl+1][self.bc]=="E") or (self.grille[self.bl+1][self.bc]=="S") or (self.grille[self.bl+1][self.bc]=="O") and (self.grille[self.bl][self.bc+1]!="E"):
            self.bl+=1
            self.mouvBall.append([self.bc,self.bl])
            self.surObj()
                
            
        self.bille()
        
    def roule(self,direc):
        self.mouvBall=[]
        #fait rouler la balle vers la droite ou la gauche autant que possible (peut dessendre de plusieurs ligne"
        if direc=="d":
            while self.grille[self.bl][self.bc+1]==" " or (self.grille[self.bl][self.bc+1]=="E") or (self.grille[self.bl][self.bc+1]=="S") or (self.grille[self.bl][self.bc+1]=="O") and (self.grille[self.bl][self.bc+1]!="E"):
                self.grille[self.bl][self.bc]=" "
                self.bc+=1
                self.mouvBall.append([self.bc,self.bl])
                self.surObj()
                Laby.gravite(self)
                
                
        if direc=="g":
            self.grille[self.bl][self.bc]=" "
            while self.grille[self.bl][self.bc-1]==" " or (self.grille[self.bl][self.bc-1]=="E") or (self.grille[self.bl][self.bc-1]=="S") or (self.grille[self.bl][self.bc-1]=="O") and (self.grille[self.bl][self.bc+1]!="E"):
                self.grille[self.bl][self.bc]=" "
                self.bc-=1
                self.mouvBall.append([self.bc,self.bl])
                self.surObj()
                Laby.gravite(self)
                
                
        print(self.mouvBall,self.bl,self.ol,self.bc,self.oc)
        self.bille()
                
    def bille(self):
        #place la bille dans la grille
        print("bille placée")
        self.grille[self.bl][self.bc]="B"    
    
    def poseObjet(self):
        #place l'objet sur la grille
        nbPair= []
        for i in range(4,self.nbl-1,2):
            nbPair.append(i)
        self.ol=random.choice(nbPair)
        self.oc=random.choice(nbPair)
        self.grille[self.ol][self.oc]="O"
        print(self.oc,self.ol)

    def surObj(self):
        #verifie si la balle est sur l'objet
        if self.bl==self.ol and self.bc==self.oc:
                self.recupO=1
                print("vous avez recuper l'objet, bravo")
        
    def __repr__(self):
        
        res=""
        for ligne in self.grille:
            res+="\n"+" ".join(ligne)
        return res



 

# methode generation : http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
