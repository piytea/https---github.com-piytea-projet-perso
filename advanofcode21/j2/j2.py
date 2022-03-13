with open('inputJ2.txt', 'r') as fichier:
    txt = fichier.readlines()

#txt=txt.split("\n")
txt=txt[:-1]
print (txt[-10:])      
              
for i in range(len(txt)):
    ##print(txt[i])
    txt[i]=txt[i].split(" ")
    txt[i][1]=int(txt[i][1])

print (txt[-10:]) 
horizontal , depth , aim =0,0,0
def pilotage():
    
   
    
    for i in txt:
        if "forward" in i:
            horizontal+= i[1]
            #print(i)
        elif "down" in i:
            depth+=i[1]
            #print(i)
        else :
            depth-=i[1]
            #print(i)
    print(horizontal,depth)
    return horizontal*depth

#print(pilotage())

def pilotageWAim():
    
    for i in txt:
        if "forward" in i:
            horizontal+= i[1]
            depth+=aim*i[1]
            #print(i)
        elif "down" in i:
            aim+=i[1]
            #print(i)
        else :
            aim-=i[1]
            #print(i)
    print(horizontal,depth)
    return horizontal*depth

#print(pilotageWAim())

with open("inputJ2.txt", 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
aim, x1, y1, x2, y2 = 0, 0, 0, 0, 0
move = {
    'forward' : lambda aim, x, y, z, part : (aim, x + z, y) if part == 1 else (aim, x + z, y + (z * aim)),
    'down'    : lambda aim, x, y, z, part : (aim, x, y + z) if part == 1 else (aim + z, x, y),
    'up'      : lambda aim, x, y, z, part : (aim, x, y - z) if part == 1 else (aim - z, x, y)
    }
for instruction, amt in data:
    aim, x1, y1 = move[instruction](aim, x1, y1, int(amt), 1)
    aim, x2, y2 = move[instruction](aim, x2, y2, int(amt), 2)
print(move["up"])
print(x1 * y1)
print(x2 * y2)
