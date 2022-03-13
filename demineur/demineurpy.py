import pygame as py
import random
#import numpy as np

py.init()
class Demineur:
# fonctions de base du jeu 
    def __init__(self,bombe,nbl,nbc,init="X"):
        """
        parametres de base d'une grille
        nbl et nbc : nb de ligne et de colonnes
        posbomb : liste avec la position ( lg,col) de chaque bombe
        tour : coordonees (lg,col) pour effectuer un tour complet autour d'une case
        restecaes: nb de cases sans bombe qu'il reste à trouver
        continu : indicatuer pur poursuivre la partie ou non
        grilleInit: grille de nbl ligne et nbc col remplie avec init (= 0 par defaut)
        """
        self.nbl=nbl
        self.nbc=nbc
        self.nbbomb=bombe
        self.grille=[[init]*self.nbc for x in range(self.nbl)]
        self.solu=[[0]*self.nbc for x in range(self.nbl)]
        self.posbomb=[]
        self.tour=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        self.restecase=self.nbl*self.nbc-self.nbbomb
        self.continu=0
        self.drapeau=0
        
    def addbomb(self):
    #place x bombe ('b') aleatoirment dans la grille et enregistre les position
        for i in range(self.nbbomb):
            bc=random.randint(0,self.nbc-1)
            bl=random.randint(0,self.nbl-1)
            while self.solu[bl][bc]=="b":
                bc=random.randint(0,self.nbc-1)
                bl=random.randint(0,self.nbc-1)
                #print("double",i)
            self.solu[bl][bc]="b"
            self.posbomb.append([bl,bc])
        #print(self.posbomb)
        
    def infobomb(self):
    #ajoute pour chaque case le nb de bombe à proximité
    
        for bmb in self.posbomb:
            for i in self.tour:
                a,b=i[0],i[1]
                nl,nc= bmb[0]+a, bmb[1]+b
                if (0<=nl<len(self.solu) and 0<=nc<len(self.solu[0])) and self.solu[nl][nc]!="b":
                    #print(bmb,nl,nc)
                    
                    self.solu[nl][nc]+=1
                    
    def nouvelprop(self):
    
        val=input("faites une proposition(ligne col (0 0)) ou drapeau:pos+d(0 0 d) : ")
        return val.split(" ")
    
    def creuse(self,case):
    #trouve les zones sans bombes à proximité   
        for i in self.tour:
                a,b=i[0],i[1]
                nl,nc= case[0]+a, case[1]+b
                if (0<=nl<len(self.solu) and 0<=nc<len(self.solu[0])) and self.solu[nl][nc]!="b"  and self.grille[nl][nc]=="X"  :
                    self.restecase-=1
                    
                    #print(self.restecase)
                    if self.solu[nl][nc]==0:
                        self.grille[nl][nc]=self.solu[nl][nc]
                        #print(nl,nc)
                        self.creuse([nl,nc])
                    else :
                        self.grille[nl][nc]=self.solu[nl][nc]
                    #print(bmb,nl,nc)
                        
    def testbomb(self,case,drapeau):
        """
        regarde si la case est sans bombe
        non : fin du jeu
        oui :
        un chiffre sur la case >>affiche les chifre
        un 0 >> regarde autour si c'est une zone 0 ( creuse)
        """
        lg=int(case[0])
        col=int(case[1])
        if drapeau==1  :
            if self.grille[lg][col]=="X":  
                self.grille[lg][col]="d"
            elif self.grille[lg][col]=="d":
                self.grille[lg][col]="X"
        else:
            #print(lg,col)
            if self.grille[lg][col]!="d" and self.grille[lg][col]=="X":
                if self.solu[lg][col]!="b" :
                    print("bon")
                    self.grille[lg][col]=self.solu[lg][col]
                    self.restecase-=1
                    #print(self.restecase)
                    if self.grille[lg][col]==0:
                        #print(lg,col)
                        self.creuse([lg,col])
                else:
                    self.grille[lg][col]=self.solu[lg][col]
                    self.continu=1
        
    def __repr__(self):
        res= "  | "+' '.join(str(i) for i in range(self.nbc))+"   \t|"+"  | "+' '.join(str(i) for i in range(self.nbc))+"|\n"
        
        for i in range(self.nbl):
            res+="\n"+str(i)+" | "+' '.join(str(val) for val in self.grille[i])+"   \t|"+str(i)+" | "+' '.join(str(val) for val in self.solu[i])+"|"

        return res
    
class DeminPyG(Demineur):
#affichage et interaction avec  pygame du jeu
    FONT = py.font.SysFont ("Times New Norman", 40)
    MEDFONT = py.font.SysFont('Corbel',50)
    SMALLFONT = py.font.SysFont('Corbel',35)
    CGAUCHE= (0,255,0)
    CDROITE=(50,0,200)
    CGRILLE=(150,0,210)
    CFOND=(0,0,0)
    CINFO=(1,0,1)
    
    print(tuple([2*x for x in CINFO]),"ggg")
    
    def __init__(self,nbomb,nbl,nbc,tailleFx,tailleFy):
        
        Demineur.__init__(self,nbomb,nbl,nbc)
        """
        nbl =nombre de lignes de la grille
        nbc =nombre de colonnes de la grille
        nbcase= nombre de cases restantes
        tailleInfo = zone de droite
        F (x/y) = fenetre entiere
        G (x/y) = espace grille
    """
        self.nbl=nbl
        self.nbc=nbc
        self.nbcase=0
        self.tailleInfo=350
        self.tailleFx=int(tailleFx+self.tailleInfo)
        self.tailleFy=tailleFy
        self.tailleGx=tailleFx
        self.tailleGy=tailleFy
        self.screen = py.display.set_mode((self.tailleFx,self.tailleFy))
        
        if self.nbl>self.nbc:
            self.nbcase=self.nbl
        else:
            self.nbcase=self.nbc

        #position et taille des boutons drapeau (pi) et creuse (dp)   
        self.tcase=self.tailleGx/self.nbcase
        self.posdpX=self.tailleGx+self.tailleInfo/2 - self.tcase-10
        self.posdpY=self.tailleInfo/10
        self.pospiX=self.tailleGx+self.tailleInfo/2 +10
        self.pospiY=self.tailleInfo/10

        
        self.jouer=True
        self.rejoue=None
        #"self.choix=True

        
        self.posReJou=(self.tailleGx+int(self.tailleInfo/4),self.tailleGy/2,self.tailleGx+int(self.tailleInfo/4) +100,self.tailleGy/2 +50)
        self.posTextResult=(self.tailleGx+int(self.tailleInfo/4),int(self.tailleGy/3),self.tailleGx+int(self.tailleInfo/4) +100,self.tailleGy/2 +50)
        print(self.posdpX, self.posdpY)

        self.posChoix= (self.tailleGx+int(self.tailleInfo/4),self.tailleGy/4 *3 ,self.tailleGx+int(self.tailleInfo/4) +100,self.tailleGy/4 *3+100)
        
    def fenetre(self):
        py.draw.rect(self.screen,(self.CFOND),(0,0,self.tailleGx,self.tailleGy))
        py.draw.rect(self.screen,(255,255,255),(self.posdpX-5,self.posdpY-5,self.tcase+10,self.tcase+10))
        py.draw.rect(self.screen,(0,200,0),(self.posdpX,self.posdpY,self.tcase,self.tcase))
        py.display.set_caption("Demineur")
        py.display.flip()
        
    def affiche_info(self):
        self.afficheText(str(self.restecase),(0,0,0,0),self.posTextResult)
        py.draw.rect(self.screen,(DeminPyG.CGAUCHE),(self.posdpX,self.posdpY,self.tcase,self.tcase))
        py.draw.rect(self.screen,(DeminPyG.CDROITE),(self.pospiX,self.pospiY,self.tcase,self.tcase))
        self.degrade()
        py.display.flip()
        
    def affiche_grille(self):
        print(self.restecase)
        #py.draw.rect(self.screen,(100,100,100),(0,0,self.tailleF,self.tailleF))
        
        #affichage de la grille et enregistrement des coordonées de chaque image
        for l in range(len(self.grille)):
            for c in range(len(self.grille[0])):
                if self.grille[l][c] == "X":
                    #print(c,l)
                    py.draw.rect(self.screen,(DeminPyG.CGRILLE),(c*self.tcase,l*self.tcase,self.tcase-2,self.tcase-2))
                    
                elif self.grille[l][c] == "b":
                    py.draw.rect(self.screen,(255,0,0),(c*self.tcase,l*self.tcase,self.tcase,self.tcase))

                elif self.grille[l][c] == "d":
                    py.draw.rect(self.screen,(DeminPyG.CDROITE),(c*self.tcase,l*self.tcase,self.tcase-2,self.tcase-2))
                    
                elif self.grille[l][c] !="b" and self.grille[l][c] !="d" and self.grille[l][c] !=0:
                    #print(0,255-int((1/(2**self.grille[l][c]))*475))
                    #py.draw.rect(self.screen,tuple([30*self.grille[l][c]*x for x in DeminPyG.CINFO]),(c*self.tcase,l*self.tcase,self.tcase,self.tcase))
                    self.afficheText(str(self.grille[l][c]),tuple([30*self.grille[l][c]*x for x in DeminPyG.CINFO]),(c*self.tcase,l*self.tcase,self.tcase,self.tcase))
                if self.grille[l][c] ==0:
                    
                    py.draw.rect(self.screen,(DeminPyG.CFOND),(c*self.tcase,l*self.tcase,self.tcase,self.tcase))

        py.display.flip() 
        
        
    def degrade(self):
        
        print(self.tailleGy/10,self.tailleGx)
        x=self.tailleGx+ (self.tailleInfo/10)
        y=2*(self.tailleInfo/10)
        z=int(8*(self.tailleGx/2550))
        t=self.tailleInfo/10
        for i in range(0,255):
            #print(int(255/(self.tailleGy/10)*4))
            py.draw.rect(self.screen,tuple([i*x for x in DeminPyG.CINFO]),(x,3*y+z*i,1.5*t,z))
            
    def afficheText(self,text,couleur,pos):
        ax,ay,bx,by=pos
        py.draw.rect(self.screen,couleur,(ax,ay,bx,by))
        textjeu = DeminPyG.FONT.render(text, True, (255,255,255))
        recttitre = py.Rect(ax,ay,bx,by)
        self.screen.blit(textjeu,(ax+self.tcase/3,ay+self.tcase/3))
        
    def contourC1(self):
        
        py.draw.rect(self.screen,(255,255,255),(self.posdpX-5,self.posdpY-5,self.tcase+10,self.tcase+10))
        py.draw.rect(self.screen,(DeminPyG.CGAUCHE),(self.posdpX,self.posdpY,self.tcase,self.tcase))                  
        py.draw.rect(self.screen,(0,0,0),(self.pospiX-5,self.pospiY-5,self.tcase+10,self.tcase+10))
        py.draw.rect(self.screen,(DeminPyG.CDROITE),(self.pospiX,self.pospiY,self.tcase,self.tcase))
        
    def contourC2(self):
        
        py.draw.rect(self.screen,(0,0,0),(self.posdpX-5,self.posdpY-5,self.tcase+10,self.tcase+10))
        py.draw.rect(self.screen,(DeminPyG.CGAUCHE),(self.posdpX,self.posdpY,self.tcase,self.tcase))                    
        py.draw.rect(self.screen,(255,255,255),(self.pospiX-5,self.pospiY-5,self.tcase+10,self.tcase+10))
        py.draw.rect(self.screen,(DeminPyG.CDROITE),(self.pospiX,self.pospiY,self.tcase,self.tcase))
    
    def jeu_choix( self):
        self.afficheText("10*10 n 20 bombes",(0,0,0), self.posChoix)
        
    def newJeu(self,nbBomb,nlg,ncol,tx,ty):
        #py.init()
        DeminPyG.__init__(self,nbBomb,nlg,ncol,tx,ty)
        #jeu=DeminPyG(nbBomb,nlg,ncol,tx,ty)
        jeu.addbomb()
        jeu.infobomb()
        jeu.fenetre()
        jeu.affiche_grille()
        jeu.affiche_info()
        print(jeu)
        jeu.joue()
        #jeu.choix()

        
    def joue(self):
        
        continuer=True
        while continuer:
            for event in py.event.get():
                if event.type == py.QUIT:
                    
                    continuer=False
                    py.display.quit()
                    
                elif event.type == py.MOUSEBUTTONDOWN:
                    pos = py.mouse.get_pos()
                    
                    a,b=pos
                    #print(a,b)
                    if self.jouer:
                        
                        if a<self.tailleGx and b<self.tailleGy :
                            #print(a//self.tcase,b//self.tcase)
                            jeu.testbomb([b//self.tcase,a//self.tcase],self.drapeau)
                            
                            #print(self.restecase)
                            jeu.affiche_grille()
                            jeu.affiche_info()
                            #print(self.restecase)
                        
                        else:
                            if self.posdpX<a<self.posdpX +self.tcase and self.posdpY<b<self.posdpY+self.tcase:
                                #print("creuse oit'gong")
                                self.contourC1()
                                self.drapeau=0
                            if self.pospiX<a<self.pospiX +self.tcase and self.pospiY<b<self.pospiY+self.tcase:
                                self.contourC2()
                                self.drapeau=1
                                
                                #print("met un drapeau")
                            #print(self.drapeau)
                            py.display.flip()
                    #print(self.posReJou)
                    if self.rejoue and a<= self.posReJou[2] and a> self.posReJou[0] and b<= self.posReJou[3] and b>= self.posReJou[1]:
                        #print("nouveau jeu")
                        self.jouer = True
                        self.rejoue=False
                        #self.continuer=False
                        
                        
                        self.newJeu(self.nbbomb,self.nbl,self.nbc,700,700)
                        py.display.quit()
                        
                        #py.display.flip()
                        
                        
                elif self.continu==1:
                    
                    self.afficheText("BOOUUUMMM",(0,0,0),self.posTextResult)
                    self.afficheText("rejouer?",(0,0,0),self.posReJou)
                    py.display.flip()
                    self.jouer=False
                    self.rejoue=True
                    #print(self.posReJou)
                    #continuer=False
                   
                elif self.restecase==0:
                    self.afficheText("Bravoo !!",(0,0,0),self.posTextResult)
                    self.afficheText("rejouer?",(0,0,0),self.posReJou)

                    py.display.flip()
                    self.jouer=False
                    self.rejoue=True
                    #print(self.posReJou)
                    #continuer=False
                        
                 
                    
                '''
                elif event.type==py.KEYDOWN:
                    if event.key==py.K_RIGHT:
                        
                        self.labyPy.rotation("d")
                    if event.key==py.K_LEFT:
                        
                        self.labyPy.rotation("g")
                    print(self.labyPy)
                '''
        py.quit()   

if __name__=="__main__":
    # ( nb bombe,nbligne,nb col, taille fen)

    jeu=DeminPyG(20,10,10,700,700)
    jeu.newJeu(10,10,10,700,700)
    """
    jeu.addbomb()
    jeu.infobomb()

    print(jeu)
    jeu.fenetre()
    jeu.affiche()
    jeu.joue()
    
    while jeu.restecase!=0 :
        print(jeu)
        test=jeu.nouvelprop()
        jeu.testbomb(test)
        if jeu.continu==1:
            print("BOUMMMM")
            break
    """
        
    
    
