with open('inputJ7.txt', 'r') as fichier:
    txt = fichier.read()
txt=txt.split(",")
for x in range(len(txt)):
    txt[x]=int(txt[x])
#print(txt)

#print(txt)
test=[16,1,2,0,4,2,7,1,2,14]
#txt=test
txt.sort()
pcrabs={}
for c in txt:
    if c in pcrabs:
        pcrabs[c]+=1
    else :
        pcrabs[c]=1
ecarts={}
for x in range(0,max(txt)+1):
    ecarts[x]=0
    for i in range(x+1):
        ecarts[x]+=i
#print(ecarts)
def part1():
    med=txt[len(txt)//2]
    sommes=[]
    for i in range(med-10,med+10):
        tot=0
        for cle, val in pcrabs.items():
            tot+=abs(cle-i)*val
        sommes.append([tot,i])
    #print(pcrabs)
    return min(sommes)
def part2():
    sommes=[]
    for i in range(400,600):
        tot=0
        for cle, val in pcrabs.items():
            #print(ecarts[abs(cle-i)])
            tot+=ecarts[abs(cle-i)]*val
        sommes.append([tot,i])
    #print(pcrabs)
    return min(sommes)
print(part1())
print(part2())
#127638
#125256
#122890
