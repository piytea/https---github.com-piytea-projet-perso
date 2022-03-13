
with open('inputJ1.txt', 'r') as fichier:
    txt = fichier.read()
#print(contenu)
txt=txt.split("\n")
for i in range(len(txt)-1):
    #print(txt[i])
    txt[i]=int(txt[i])
    
print (txt[:10])
diff=0
monte=0
descend=0
print(txt[-10:])
for i in range(0,len(txt)-2):
    #print(i,txt[i])
    if int(txt[i+1])-int(txt[i])> 0:
        monte+=1
        #print("monte")
    else:
        descend+=1
        #print("descend")
    diff=   int(txt[i+1])-int(txt[i])
    
print( monte,descend)
monte=0
descend=0
print(txt[-7:])
for i in range(0,len(txt)-4,1):
    
    #print(i,txt[i],i+3)
    FEN2=txt[i+1]+txt[i+1+1]+txt[i+1+2]
    fen1=txt[i]+txt[i+1]+txt[i+2]
    if FEN2-fen1 > 0:
        monte+=1
        #print("monte")
    else:
        descend+=1
        #print("descend")
    diff=   int(txt[i+1])-int(txt[i])
print( monte,descend)
