import pygame as py
import grille as gr
import math


class SpBalle(py.sprite.Sprite):
    #Classe concernant la gestion de la balle
    def __init__(self,col,lg,img,cx,cy):
        py.sprite.Sprite.__init__(self)
        self.image=img
        self.cx=cx
        self.cy=cy
        self.dx,self.dy=col,lg
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(col,lg)
       
    def update(self,px,py,angle):
        print(self.image,int(angle))
        #self.image = py.transform.rotate(self.image,int(-self.angle))
        self.calcrotate(px,py,angle)
        self.rect=self.rect.move(self.dx,self.dy)

    def calcrotate(self,x,y,angle):
        angle=math.radians(angle)
        self.dx=(self.cx + math.cos(angle) * (x - self.cx) - math.sin(angle) * (y - self.cy))-self.rect.x
        self.dy=(self.cy + math.sin(angle) * (x - self.cx) + math.cos(angle) * (y - self.cy))-self.rect.y
        
    #def update(self):
       
        
    
class Labypygame(gr.Laby):
    
    MUR = py.image.load("img/mur.png")
    ARR = py.image.load("img/humain.png")
    FOND = py.image.load("img/fond_espace.png")
    BALLE = py.image.load("img/vaisseau.png")
    DEP = py.image.load("img/alien.png")
    BORD = py.image.load("img/mur.png")
    OBJET = py.image.load("img/bidon.png")
    FUMEE = py.image.load("img/fumee.png")
    ANGLE=90/4
    #POINT = py.image.load("img/point.png")
    def __init__(self,nbl,nbc,tailleF,):
        
        gr.Laby.__init__(self,nbl,nbc)
              
        
        self.nb_case = len(self.grille[0])
        self.long=tailleF -100
        self.larg=tailleF -100
        self.case=self.long/nbc
        self.screen = py.display.set_mode((tailleF,tailleF))
        self.mur = py.transform.scale(Labypygame.MUR, (int(self.long/self.nb_case), int(self.larg/self.nb_case)))
        self.arr = py.transform.scale(Labypygame.ARR, (int(self.long/self.nb_case), int(self.larg/self.nb_case)))
        self.balle = py.transform.scale(Labypygame.BALLE, (int(self.long/self.nb_case), int(self.larg/self.nb_case)))
        self.fond = py.transform.scale(Labypygame.FOND, (tailleF+100, tailleF+100))
        self.depart = py.transform.scale(Labypygame.DEP,((int(self.long/self.nb_case), int(self.larg/self.nb_case))))
        self.bordure = py.transform.scale(Labypygame.BORD,((int(self.long/self.nb_case), int(self.larg/self.nb_case))))
        self.objet = py.transform.scale(Labypygame.OBJET,((int(self.long/self.nb_case), int(self.larg/self.nb_case))))
        self.fondBalle = py.transform.scale(Labypygame.FUMEE,((int(self.long/self.nb_case), int(self.larg/self.nb_case))))
        #self.point = py.transform.scale(Labypygame.POINT,((int(self.long/self.nb_case), int(self.larg/self.nb_case))))
        print(self.fondBalle)
        self.deca = 50
        self.tailleF= tailleF
        self.ox = (self.long)/2 -self.long/self.nb_case/2 +self.deca
        self.oy = (self.long )/2 -self.long/self.nb_case/2 +self.deca
        self.angle=0
        self.anglebille=0
        self.nbrota=int(90/Labypygame.ANGLE)
        self.cTeurRota=0
        self.spriteBall = py.sprite.Group()
        self.dicoGrille={"mur" : [self.mur] ,"arr" : [self.arr] , "bor" : [self.bordure], "bille" : [self.balle], "dep" : [self.depart], "obj" : [self.objet]}
        
        
    def fenetre(self):
        self.fondnoir = py.draw.rect(self.screen,(0,0,0),(0,0,self.tailleF,self.tailleF))
        self.p_fond = self.fond.get_rect()
        self.screen.blit(self.fond,self.p_fond)
        py.display.set_caption("laby")
        py.display.flip()

    def affiche(self):
        #affichage de la grille et enregistrement des coordonées de chaque image
        for l in range(len(self.grille)):
            for c in range(len(self.grille[0])):
                if self.grille[l][c] == "p":
                    img=self.mur
                    self.rect=img.get_rect()
                    self.rect=self.rect.move(self.case*c+self.deca,self.case*l+self.deca)
                    self.dicoGrille["mur"].append(self.rect)
                    self.screen.blit(img,self.rect)
                    
                elif self.grille[l][c] == "X":
                    img=None
                elif self.grille[l][c] == "E":
                    img=self.depart
                    self.rect=img.get_rect()
                    self.rect=self.rect.move(self.case*c+self.deca,self.case*l+self.deca)
                    self.dicoGrille["dep"].append(self.rect)
                    self.screen.blit(img,self.rect)
                    
                elif self.grille[l][c] == "S":
                    img=self.arr
                    self.rect=img.get_rect()
                    self.rect=self.rect.move(self.case*c+self.deca,self.case*l+self.deca)
                    self.dicoGrille["arr"].append(self.rect)
                    self.screen.blit(img,self.rect)

                elif self.grille[l][c] == "O":
                    img=self.objet
                    self.rect=img.get_rect()
                    self.rect=self.rect.move(self.case*c+self.deca,self.case*l+self.deca)
                    self.dicoGrille["obj"].append(self.rect)
                    self.screen.blit(img,self.rect)
                    
                elif self.grille[l][c] == "B":
                    img=SpBalle(self.case*c+self.deca,self.case*l+self.deca,self.balle,self.ox,self.oy)
                    self.dicoGrille["bille"].append(img.rect)
                    self.screen.blit(img.image,img.rect)
                    self.spriteBall.add(img)
            
                
   
    def calcrotate(self,a,b,angle):
        #calcul de nouvelles coordonées en fonction d'un angle
        angle=math.radians(angle)
        px = a
        py = b
        x= self.ox + math.cos(angle) * (px - self.ox) - math.sin(angle) * (py - self.oy) 
        y= self.oy + math.sin(angle) * (px - self.ox) + math.cos(angle) * (py - self.oy)
        return x,y
        

    def rotation(self,direc):
        #actualise les angle et deplacements
        
        self.mouvBall=[]
        self.angle += Labypygame.ANGLE if direc == "d" else -Labypygame.ANGLE
        self.anglebille += Labypygame.ANGLE if direc == "d" else -Labypygame.ANGLE
        self.cTeurRota+=1 if direc == "d" else -1
        
        #gestion rotation et deplacement de la balle
        if self.angle %90==0 and self.cTeurRota%self.nbrota==0 and self.cTeurRota!=0 :
            self.rotation90(direc)
            self.cTeurRota=0
            self.anglebille=0
        if self.angle%90!=0:
            self.roule(direc)

        #affichage de la grille
        self.fenetre()
        for cle,val in self.dicoGrille.items():
            if cle != "bille" :
                if (cle=="obj" and self.recupO!=0):
                    pass
                else:
                    for i in val[1:]:
                        self.img = py.transform.rotate(val[0],-self.angle)
                        pa,pb = self.calcrotate(i[0],i[1],self.angle)
                        self.p_img3 = self.img.get_rect()
                        self.p_img3 = self.p_img3.move((pa),(pb))   
                        self.screen.blit(self.img,self.p_img3)

        #affichage de la balle            
        if len(self.mouvBall)>0  :
            #la balle se deplace dans la grille
            for coord in self.mouvBall:
                #animation de la balle 
                self.spriteBall.update(coord[0]*self.case+self.deca,coord[1]*self.case+self.deca,self.anglebille)
                self.spriteBall.draw(self.screen)
                py.display.flip()
                
                #ralenti le mouvement
                py.time.delay(int(10*self.nbrota))
                
                #dessine un rectangle noir par dessus la balle (pour "cacher" la trace
                self.img = py.transform.rotate(self.fondBalle,-self.angle)
                a,b=self.calcrotate(coord[0]*self.case+self.deca,coord[1]*self.case+self.deca,self.anglebille)
                self.screen.blit(self.img,(a,b))
                py.display.flip()
            self.spriteBall.draw(self.screen)
        else:
            #la balle reste au meme endroit dans la grille
            self.spriteBall.update(self.bc*self.case+self.deca,self.bl*self.case+self.deca,self.anglebille)
            self.spriteBall.draw(self.screen)

