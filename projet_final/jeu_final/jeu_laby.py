import pygame as py
from pygame.locals import *
import class_pygame as cp
import grille as gr
from datetime import timedelta, datetime, date, time

py.init()
class Jeu:
    # les lignes qui suivent contiennent tous les paramètres de jeu
    NIV1=10
    #poloces d'écritures:
    FONT = py.font.SysFont ("Times New Norman", 60)
    MEDFONT = py.font.SysFont('Corbel',50)
    SMALLFONT = py.font.SysFont('Corbel',35)
    #couleurs:
    ROUGE = (233,69,36)
    VERT = (81,216,30)
    BLEU = (14,74,204)
    BLANC = (255,255,255)
    #imges:
    IMG_FOND = py.image.load("img/fond_espace.jpg")
        
    
    def __init__(self,tailleF):

        self.tailleF=tailleF
        self.labyPy= None
        self.chrono =datetime.combine(date.today(), time(0, 0))
        self.dt=0
        self.label=Jeu.FONT.render(self.chrono.strftime("%M : %S : %f "),True, Jeu.BLANC)
        self.joueur= None
        self.classement = None
        self.temp = 0
        self.position_fond = (0,0,self.tailleF,self.tailleF)

        #nouveau menu
        self.fen = py.display.set_mode((self.tailleF,self.tailleF))
        fen_rec = self.fen.get_rect()
        self.clock = py.time.Clock()
        self.fd_color = (50, 70, 90)
        self.img_fond = py.transform.scale(Jeu.IMG_FOND, (fen_rec.right, fen_rec.bottom))
        #permet d'activer ou de désactiver certains bouttons.
        self.sauv = 0
        self.nbniv = 0
        self.gojouer = 1
        self.golevel = 0
        self.gofin = 0
        self.goscore = 0
        self.nb_joueur = 0
        #liste de bouttons
        self.b_quit = None
        self.b_jouer = None
        self.b_level = None
        self.b_fin = None
        self.b_score = None
        self.b_aff_score = None

        #variables pour les textes des bouttons du menu
        self.long_title = 300
        self.larg_title = 100
        self.long_but = 205
        self.larg_but = 80
        self.croix_p1 = self.tailleF - 60
        self.croix_p2 = self.tailleF - 40
        self.dep_title = (self.tailleF-self.long_title)/2
        self.dep_txt = (self.tailleF-self.long_but)/2
        self.long_ask = 150
        self.dep_but_oui = (self.tailleF - (self.long_ask*2+75))/2
        self.dep_but_non = self.dep_but_oui + self.long_ask + 75

    def miseàjour(self):
        #charge les donées de l'ancien classement
        fichier = open("scores.txt", "r")
        lignes = fichier.readlines()
        new = dict(eval(lignes[0]))
        self.classement = new
        print(self.classement)

    def sauvegarde(self):
        #enregistre les données du nouveau classement
        with open("scores.txt", "w") as filout:
            filout.write(str(self.classement))
        

    def menu(self):
        #affiche le menu
        self.gofin = 0
        texttitre = Jeu.FONT.render("LABYRINTHE", True, Jeu.BLANC)
        textjeu = Jeu.FONT.render("JOUER", True, Jeu.BLANC)
        recttitre = py.Rect((self.tailleF-self.long_title)/2,100,self.long_title,self.larg_title)
        rectjeu = py.Rect(self.dep_txt,210,self.long_but,self.larg_but)
        
        self.b_quit = [[Jeu.ROUGE,(self.croix_p1,20),(self.croix_p2,40),10],
                       [Jeu.ROUGE,(self.croix_p2,20),(self.croix_p1,40),10]]
        self.b_jouer = [[texttitre, recttitre, Jeu.ROUGE],
                        [textjeu, rectjeu, Jeu.ROUGE]]

        self.fen.blit(self.img_fond,self.position_fond) 
        for i in range(len(self.b_quit)):
            self.croix = py.draw.line(self.fen, self.b_quit[i][0],self.b_quit[i][1],self.b_quit[i][2],self.b_quit[i][3])
        for i in range(0,len(self.b_jouer)):
            py.draw.rect(self.fen, self.b_jouer[i][2], self.b_jouer[i][1])
        self.fen.blit(self.b_jouer[0][0], (self.dep_title+10,130,self.long_title,self.larg_title))
        self.fen.blit(self.b_jouer[1][0], (self.dep_txt+30,230,self.long_but,self.larg_but))
        py.display.flip()   
                           
                            
    def level(self):
     #affiche les bouttons de niveaux
        self.gojouer = 0
        textlevel1 = Jeu.SMALLFONT.render("Niveau 1", True, Jeu.BLANC)
        textlevel2 = Jeu.SMALLFONT.render("Niveau 2", True, Jeu.BLANC)
        textlevel3 = Jeu.SMALLFONT.render("Niveau 3", True, Jeu.BLANC)
        textscore = Jeu.SMALLFONT.render("Scores", True, Jeu.BLANC)
        rectlevel1 = py.Rect(self.dep_txt,300,self.long_but,self.larg_but)
        rectlevel2 = py.Rect(self.dep_txt,400,self.long_but,self.larg_but)
        rectlevel3 = py.Rect(self.dep_txt,500,self.long_but,self.larg_but)
        rectscore = py.Rect(self.dep_txt,600,self.long_but,self.larg_but)
        self.b_level = [[textlevel1, rectlevel1, Jeu.ROUGE],
                        [textlevel2, rectlevel2, Jeu.ROUGE],
                        [textlevel3, rectlevel3, Jeu.ROUGE],
                        [textscore, rectscore, Jeu.ROUGE]]

        self.fen.blit(self.img_fond,self.position_fond) 
        for i in range(len(self.b_quit)):
            self.croix = py.draw.line(self.fen, self.b_quit[i][0],self.b_quit[i][1],self.b_quit[i][2],self.b_quit[i][3])
        py.draw.rect(self.fen, self.b_jouer[0][2], self.b_jouer[0][1])
        self.fen.blit(self.b_jouer[0][0], (self.dep_title+10,130,self.long_title,self.larg_title))
        for i in range(0,len(self.b_level)):
            py.draw.rect(self.fen, self.b_level[i][2], self.b_level[i][1])
        self.fen.blit(self.b_level[0][0], (self.dep_txt+37,320,self.long_but,self.larg_but))
        self.fen.blit(self.b_level[1][0], (self.dep_txt+37,420,self.long_but,self.larg_but))
        self.fen.blit(self.b_level[2][0], (self.dep_txt+37,520,self.long_but,self.larg_but))
        self.fen.blit(self.b_level[3][0], (self.dep_txt+53,620,self.long_but,self.larg_but))
        py.display.flip()
        

    def victoire(self):
        #affichage de fin de la partie et demande si on sauvegarde la partie
        textbravo = Jeu.SMALLFONT.render("Bravo !!! Vous avez fini le niveau.", True, Jeu.BLANC)
        textask = Jeu.SMALLFONT.render("Voulez vous enregistrer votre temps ?", True, Jeu.BLANC)
        textoui = Jeu.SMALLFONT.render("Oui", True, Jeu.BLANC)
        textnon = Jeu.SMALLFONT.render("Non", True, Jeu.BLANC)
        rectbravo = py.Rect((self.tailleF-550)/2,260,550,self.larg_but)
        rectask = py.Rect((self.tailleF-600)/2,360,600,self.larg_but)
        rectoui = py.Rect(self.dep_but_oui,470,self.long_ask,self.larg_but)
        rectnon = py.Rect(self.dep_but_non,470,self.long_ask,self.larg_but)

        self.b_fin = [[textbravo, rectbravo, Jeu.BLEU],
                    [textask, rectask, Jeu.BLEU],
                    [textoui, rectoui, Jeu.VERT],
                    [textnon, rectnon, Jeu.ROUGE]]
        
        self.fen.blit(self.img_fond,self.position_fond) 
        for i in range(0,len(self.b_fin)):
            py.draw.rect(self.fen,self.b_fin[i][2],self.b_fin[i][1])
        self.fen.blit(self.b_fin[0][0],((self.tailleF-550)/2+50,280,self.long_but,self.larg_but))
        self.fen.blit(self.b_fin[1][0],((self.tailleF-600)/2+25,380,self.long_but,self.larg_but))
        self.fen.blit(self.b_fin[2][0],(self.dep_but_oui+45,495,self.long_but,self.larg_but))
        self.fen.blit(self.b_fin[3][0],(self.dep_but_non+45,495,self.long_but,self.larg_but))
        py.display.flip()
        self.clock.tick(15)

    def nomjoueur(self):
        #enregistre le nom du joueur
        #partie de code inspirée de: https://openclassrooms.com/forum/sujet/input-sous-pygame
        self.fen.blit(self.img_fond,self.position_fond)     
        prompt = Jeu.MEDFONT.render('Entrez votre prénom : ', True, Jeu.ROUGE)
        prompt_rect = prompt.get_rect(center=(self.tailleF/2-80,self.tailleF/2))
        user_input_value = ""
        user_input = Jeu.MEDFONT.render(user_input_value, True, Jeu.VERT)
        user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
         
        continuer = True
        while continuer:
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key in (py.K_RETURN, py.K_KP_ENTER):
                        continuer = False
                    elif event.key == py.K_BACKSPACE:
                        user_input_value = user_input_value[:-1]
                    else:
                        user_input_value += event.unicode
                    user_input = Jeu.MEDFONT.render(user_input_value, True, Jeu.VERT)
                    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)
 
            self.clock.tick(30)
            self.fen.blit(self.img_fond,self.position_fond)     
            self.labyPy.screen.blit(prompt, prompt_rect)
            self.labyPy.screen.blit(user_input, user_input_rect)
            py.display.flip()
            
        self.joueur = user_input_value
        self.fen.blit(self.img_fond,self.position_fond)
        self.ajoutscore()
        self.gojouer = 1
        self.menu()

    def score(self):
        #affichage de la fenêtre pour visualiser les scores
        self.gojouer = 0
        self.goscore = 1
        textscore = Jeu.FONT.render("Scores", True, Jeu.BLANC)
        textlevel1 = Jeu.SMALLFONT.render("Niveau 1", True, Jeu.BLANC)
        textlevel2 = Jeu.SMALLFONT.render("Niveau 2", True, Jeu.BLANC)
        textlevel3 = Jeu.SMALLFONT.render("Niveau 3", True, Jeu.BLANC)
        textmenu = Jeu.SMALLFONT.render("Menu", True, Jeu.BLANC)
        rectscore = py.Rect(self.dep_title,100,self.long_title,self.larg_title)
        rectlevel1 = py.Rect(60,275,self.long_but,self.larg_but)
        rectlevel2 = py.Rect(60,375,self.long_but,self.larg_but)
        rectlevel3 = py.Rect(60,475,self.long_but,self.larg_but)
        rectmenu = py.Rect(60,575,self.long_but,self.larg_but)
        self.b_score = [[textlevel1, rectlevel1, Jeu.ROUGE],
                        [textlevel2, rectlevel2, Jeu.ROUGE],
                        [textlevel3, rectlevel3, Jeu.ROUGE],
                        [textmenu, rectmenu, Jeu.ROUGE]]
        
        self.fen.blit(self.img_fond,self.position_fond)
        py.draw.rect(self.fen,Jeu.ROUGE,rectscore)
        self.fen.blit(textscore,(self.dep_title+80,130,self.long_title,self.larg_title))
        for i in range(len(self.b_quit)):
            self.croix = py.draw.line(self.fen, self.b_quit[i][0],self.b_quit[i][1],self.b_quit[i][2],self.b_quit[i][3])
        for i in range(len(self.b_score)):
            py.draw.rect(self.fen,self.b_score[i][2],self.b_score[i][1])
            
        self.fen.blit(self.b_score[0][0],(100,300,self.long_but,self.larg_but))
        self.fen.blit(self.b_score[1][0],(100,400,self.long_but,self.larg_but))
        self.fen.blit(self.b_score[2][0],(100,500,self.long_but,self.larg_but))
        self.fen.blit(self.b_score[3][0],(115,600,self.long_but,self.larg_but)) 

        py.display.flip()

    def affichage_score(self,nblevel):
        #affiche les scores avec le nom du joueur et le temps:
        Jeu.score(self)
        niveau = ("niv"+str(nblevel))
        if(len(self.classement[niveau]) == 0):
                textaff_1 = Jeu.MEDFONT.render("Il n'y a pas de", True, Jeu.ROUGE)
                textaff_2 = Jeu.MEDFONT.render("temps enregistré.", True, Jeu.ROUGE)
                self.fen.blit(textaff_1, (300,300,self.long_but,self.larg_but))
                self.fen.blit(textaff_2, (300,400,self.long_but,self.larg_but))
        for i in range(0,len(self.classement[niveau])):
            if(len(self.classement[niveau][i]) == 2):
                txt = self.classement[niveau][i][0]+": "+str(self.classement[niveau][i][1])
                textaff = Jeu.MEDFONT.render(txt, True, Jeu.ROUGE)
                self.fen.blit(textaff, (300,75*i+300,self.long_but,self.larg_but))
        py.display.flip()
        
    def ajoutscore(self):
        #ajoute les scores dans le dico
        ancien_temps = 0
        chaine_carac = ("niv"+str(self.nbniveau))
        
        #vérifie si il y à déjà un joueur avec ce nom
        for i in self.classement:
            for j in range(0,len(self.classement[i])):
                if self.joueur in self.classement[i][j]:
                    ancien_temps = self.classement[i][j][1]
                    self.nb_joueur = 1
                    
        #si il y a un jour il compare les 2 temps
        #pour enregistrer que le plus petit temps
        if self.nb_joueur == 1:
            if (self.temp < ancien_temps and len(self.temp)<=len(ancien_temps)):
                for i in self.classement:
                    for j in range(0,len(self.classement[i])):
                        if self.joueur in self.classement[i][j]:
                            self.classement[i][j][1] = self.temp
        #si le joueur n'est pas connu, le temps est automatiquemeny enregistré
        else:
            liste_temp = [self.joueur,self.temp]
            self.classement[chaine_carac].append(liste_temp)
        self.nb_joueur = 0
        print(self.classement)
        
   
    def update_chrono(self):
        """Mise à jour du temps écoulé.
        dt est le nombre de millisecondes"""
        
        old_chrono = self.chrono
        self.chrono += timedelta(milliseconds=self.dt)
        if old_chrono != self.chrono:
            self.label = Jeu.FONT.render(self.chrono.strftime("%M : %S : %f "),
                       True, Jeu.BLANC)

    def jouer(self,nbl,nbc,niv):
        #fonction qui permet de lancer le labyrinthe, créer un score
        self.labyPy=cp.Labypygame(nbl,nbc,self.tailleF)
        print(self.labyPy)
        self.labyPy.chemin(2,2)
        self.labyPy.bille()
        self.labyPy.entresors()
        self.labyPy.fenetre()
        self.labyPy.gravite()
        self.labyPy.poseObjet()
        self.labyPy.affiche()
        self.chrono =datetime.combine(date.today(), time(0, 0))
        temp=py.time.Clock()
        
        continuer=True
        while continuer:
            for event in py.event.get():
                if event.type == QUIT:   
                    py.draw.rect(self.labyPy.screen,(0,0,0),(0,0,self.labyPy.tailleF,self.labyPy.tailleF+100))
                    self.gojouer = 1
                    Jeu.menu(self)
                    continuer=False  
                elif event.type==py.KEYDOWN:
                    if event.key==py.K_RIGHT:
                        
                        self.labyPy.rotation("d")
                    if event.key==py.K_LEFT:
                        
                        self.labyPy.rotation("g")
                    print(self.labyPy)
                       

            self.dt = temp.tick(60)
            py.draw.rect(self.labyPy.screen,(0,0,0),(0,self.tailleF-50,self.tailleF,self.tailleF))
            self.labyPy.screen.blit(self.label,(100,self.labyPy.tailleF-50))
            Jeu.update_chrono(self)
            py.display.update()
            
            if self.labyPy.bl ==self.labyPy.nbl-3 and self.labyPy.bc==self.labyPy.nbc-2 and self.labyPy.recupO!=0:
                py.time.delay(500)
                self.labyPy.recupO=0
                continuer=False

                self.temp = str(str(self.chrono.minute)+":"+str(self.chrono.second)+":"+str(self.chrono.microsecond))
                py.draw.rect(self.labyPy.screen,(0,0,0),(0,0,self.labyPy.tailleF,self.labyPy.tailleF))
                self.nbniveau = niv
                self.gofin = 1
                self.golevel = 0
                Jeu.victoire(self)
        

    def souris(self):
        #fonction principale
        #capte les clics sur le menu, interagit avec le joueur
        continuer = True
        while continuer:
            for event in py.event.get():
                #l'événement clic de la souris
                if event.type == py.MOUSEBUTTONDOWN:
                    #toutes les variables self.go... servent à bloquer les boutons ou à les débloquer.
                    #si les varibles sont égales à 1, les boutons sont activés et si c'est égals à 0, ils sont bloqués.
                    
                    #verification  bouton Jouer du menu est debloquer
                    if self.gojouer == 1: 
                        if self.b_jouer[1][1].collidepoint(event.pos):
                            self.golevel = 1 
                            self.level()
                        elif self.croix.collidepoint(event.pos):
                            self.sauvegarde()
                            continuer= False
                            
                    #test pour fermer le jeu.
                    elif self.croix.collidepoint(event.pos):
                        Jeu.sauvegarde(self) # sauvegarde des scores
                        continuer= False
                        py.display.quit()

                        
                    #test pour lancer un niveau
                    elif self.golevel == 1:
                        #lance le en fonction du clic.
                        if self.b_level[0][1].collidepoint(event.pos):
                            Jeu.jouer(self,11,11,1)
                            self.gofin = 1
                        elif self.b_level[1][1].collidepoint(event.pos):
                            Jeu.jouer(self,15,15,2)
                            self.gofin = 1
                        elif self.b_level[2][1].collidepoint(event.pos):
                            Jeu.jouer(self,21,21,3)
                            self.gofin = 1
                            
                        #clic sur le bouton score:ouverture affichage des scores.
                            
                        elif self.b_level[3][1].collidepoint(event.pos):
                            self.golevel = 0
                            Jeu.score(self)
                            
                    #test pour l'affichage des scores
                    elif self.goscore == 1:
                        #affichage des temps de chaque joueur en fonction du niveau du clic.
                        if self.b_score[0][1].collidepoint(event.pos):
                            Jeu.affichage_score(self,1)    
                        elif self.b_score[1][1].collidepoint(event.pos):
                            Jeu.affichage_score(self,2)
                        elif self.b_score[2][1].collidepoint(event.pos):
                            Jeu.affichage_score(self,3)
                            
                        #retourne au Menu,active les boutons du menu et déactive ceux des Scores.
                        elif self.b_score[3][1].collidepoint(event.pos):
                            self.goscore = 0
                            self.gojouer = 1
                            self.menu()
                            
                    #fin du niveau : test enregistrment des scores:
                    elif self.gofin == 1:
                        
                        #oui: demande le nom du joueur,
                        if self.b_fin[2][1].collidepoint(event.pos):
                                self.sauv = 1
                                self.nomjoueur()
                        #non: retourne au menu.
                        elif self.b_fin[3][1].collidepoint(event.pos):
                                self.gojouer = 1
                                self.menu()

      
if __name__=="__main__":
    py.init()
    
    continuer = True
    game=Jeu(800)

    #met à jour les scores
    game.miseàjour()

    #lance la fenetre de jeu
    game.menu()

    #lance l'interaction avec le joueur
    game.souris()
    #enregistre les scores
    game.sauvegarde()
   
    py.quit()
    print ("Fin du jeu")

    
