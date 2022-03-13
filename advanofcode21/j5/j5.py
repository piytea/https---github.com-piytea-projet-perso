with open('inputJ5.txt', 'r') as fichier:
    txt = fichier.readlines()
for i in range(len(txt)):
    txt[i]=txt[i].split("\n")
    txt[i]=txt[i][0]
    val=txt[i].split("->")
    txt[i]=[]
    #print(val[0],val[1])
    txt[i].append(val[0].split(","))
    txt[i].append(val[1].split(","))
    #print(txt[i])
#txt=txt.split("\n")
val1=[]
for i in txt:
    #print(i,i[0][0],i[1][0])
    if int(i[0][0])==int(i[1][0]) or int(i[0][1])==int(i[1][1]) :
        val1.append(i)
print(val1[:5],len(txt))

print(max(max(max(val1))),"xx")
#board= [[[0] for i in range(int(max(max(max(val1)))))] for x in range(int(max(max(max(val1)))))]
#print(board[:3])

def vents():
    passage=[]
    doubleP=[]
    for i in range(len(val1)):
        x1=int(val1[i][0][0])
        x2=int(val1[i][1][0])
        y1=int(val1[i][0][1])
        y2=int(val1[i][1][1])
        #print(val1[i])
        if x1==x2:
            if y1>y2:
                #print(int(val1[i][0][1])-int(val1[i][1][1]))
                passage,doubleP=passagex(y1,y2,x1,"x",passage,doubleP)
            else:
                passage,doubleP=passagex(y2,y1,x1,"x",passage,doubleP)
        else:
            if x1>x2:
                passage,doubleP=passagex(x1,x2,y1,"y",passage,doubleP)
            else:
                passage,doubleP=passagex(x2,x1,y1,"y",passage,doubleP)
        
            #print("xx")
            #for pt i range(i[0][1])==int(i[1][1])
    return len(doubleP)
        
def passagex(val1,val2,valfixe,xy,passage,doubleP):
    
    for pt in range(val1-val2):
        if xy=="x":
            pos=[valfixe,val2+pt]
        else:
            pos=[val2+pt,valfixe]
        #print(board[i][int(val1[i][0][1])+pt][0])
        if pos in passage and pos not in doubleP:
            doubleP.append(pos)
        else:
            passage.append(pos)
    return passage,doubleP
print(vents())        
for  i in range (3,0, 3-3+1):
    print(i)
    
from typing import DefaultDict

def load(path, diagonal=False):
    with open(path, "r") as f:
        raw = [s.strip() for s in f.readlines()]
    data = DefaultDict(lambda : 0)
    for trajectory in raw:
        start, end = trajectory.split(" -> ")
        x1,y1 = (int(x) for x in start.split(","))
        x2,y2 = (int(x) for x in end.split(","))
        dx = x2-x1
        dy = y2-y1
        d = max(abs(dx), abs(dy))
        dx = 0 if dx == 0 else dx//abs(dx) 
        dy = 0 if dy == 0 else dy//abs(dy)
        if not diagonal and (dx != 0 and dy != 0): continue
        for i in range(d+1):
            data[(x1+i*dx,y1+i*dy)]+=1
    return data

def part1(data):
    return sum(data[c] >= 2 for c in data.keys())

def part2(data):
    return sum(data[c] >= 2 for c in data.keys())

#assert part1(load("test1.txt")) == 5
print(part1(load("inputJ5.txt")))
#assert part2(load("test1.txt", diagonal=True)) == 12
print(part2(load("inputJ5.txt", diagonal=True)))
#5697
#5161
