with open('inputJ4.txt', 'r') as fichier:
    txt = fichier.readlines()
puzzle="""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".splitlines()
#txt=puzzle
tirage=txt[0].split(",")
print(tirage)
totgrilles=[]
#print(tirage[0])
grille=[]
for i in range (len(txt)):
    txt[i]=txt[i].split("\n")
    txt[i]=txt[i][0]
    txt[i]=txt[i].split(" ")
    
    for x in  range(txt[i].count("")) :
        txt[i].remove("")
        
    if len(txt[i])==0:
        totgrilles.append(grille)
        grille=[]
    else:
        grille.append(txt[i])
totgrilles.append(grille) 

totgrilles.remove(totgrilles[0])
totgrilles.remove(totgrilles[0])
print(totgrilles)
#print(len(totgrilles))
def joue():
    for nb in tirage:
        #print(nb)
        for  grille in range(len( totgrilles)):
            grille1= totgrilles[grille]
            #print(grille1)
            for l in range(len(grille1)):
                ligne=grille1[l]
                if nb in ligne:   
                    
                    totgrilles[grille][l][ligne.index(str(nb))]="b"
            #print(totgrilles[grille])
            if verif(totgrilles[grille])==True:
                return totgrilles[grille], nb,grille1,grille
                    
                    
#print("\n",totgrilles[5:])
def verif(grille):
    
    for i in range(len(grille)):
        ligne=0
        col=0
        #print(grille[i])
        for j in range(len(grille[0])):
            if grille[i][j]=="b":
                ligne+=1
            
            if grille[j][i]=="b":
                col+=1
            #print(grille[j][i])
        
        return ligne==5 or col==5
finalg, chiffre, pos, cc= joue()
res=0
#print(finalg,pos,"\n",joue())
print(joue())
#print(finalg,)

for i in finalg:
    
    for j in range(i.count('b')):
        i.remove('b')
    #print(i)
    for x in i:
        res+=int(x)
   
print(res,chiffre,cc)
    
#print(  totgrilles[0][0].index(str(10)))
#print(joue())

#print(totgrilles[66])
#29097



from itertools import chain

    
class Day4:
    def __init__(self, data):
        numbers, *boards = data.split('\n\n')
        *self.numbers, = map(int, numbers.split(','))
        self.boards = [[[int(n) for n in row.split()] for row in board.splitlines()] for board in boards]
        self.winning_score = self.find_winning_score()
        self.losing_score = self.find_losing_score()

    def find_winning_score(self):
        called = []
        for number in self.numbers:
            called.append(number)
            for board in self.boards:
                if any(set(line) < set(called) for line in chain(board, zip(*board))):
                    unmarked = {n for row in board for n in row} - set(called)
                    print(board)
                    return sum(unmarked) * number

    def find_losing_score(self):
        called = self.numbers.copy()
        while called:
            last = called.pop()
            for board in self.boards:
                if not any(set(line) < set(called) for line in chain(board, zip(*board))):
                    unmarked = {n for row in board for n in row} - {last, *called}
                    return sum(unmarked) * last


test_data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with open('inputJ4.txt') as f:
    data = f.read()
    
day4_test = Day4(test_data)
assert day4_test.winning_score == 4512
assert day4_test.losing_score == 1924

day4 = Day4(data)
print('Part 1:', day4.winning_score)
print('Part 2:', day4.losing_score)

