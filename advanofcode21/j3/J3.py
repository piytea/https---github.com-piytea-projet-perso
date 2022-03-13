with open('inputJ3.txt', 'r') as fichier:
    txt = fichier.readlines()

#txt=txt.split("\n")
txt=txt[:-1]
print(txt[:10])
for i in range(len(txt)):
    ##print(txt[i])
    txt[i]=txt[i].split("\n")
    txt[i]=txt[i][0]
print(txt[:10])
print(len(txt),len(txt[0]))

def part1():
    gama=""
    delta=""
    for bit in range(len(txt[0])):
        major=0
        for pos in range(len(txt)):
            major+=int(txt[pos][bit])
                       
        if major > len(txt)//2 :
            gama+="1"
            #print(gama)
        else: gama+="0"
    for l in gama:
        if l=="0":
            delta+="1"
        else:
            delta+="0"
    #print(int(gama,2),int(delta,2))
    
    return gama,delta,int(gama,2)*int(delta,2)

plusval,moinval,total=part1()
print(plusval,moinval,total)
def part2():
    possibleGenerator=txt
    possibleScrubber=txt
    for bit in range(len(txt[0])):
        generator=[]
        scrubber=[]
        mx=""
        mini=""
        nb0=0
        nb1=0
        for pos in range(len(possibleGenerator)):
            #print(txt[pos][bit])
            if possibleGenerator[pos][bit]=="1":
                nb1+=1
            if possibleGenerator[pos][bit]=="0":
                nb0+=1
        print(nb0,nb1,bit)
        if nb0>nb1:
            mx="0"
        else:
            mx="1"
        
        nb0=0
        nb1=0
        for pos in range(len(possibleScrubber)):
            if possibleScrubber[pos][bit]=="1":
                nb1+=1
            if possibleScrubber[pos][bit]=="0":
                nb0+=1
        if nb1<nb0:
            mini="1"
        else:
            mini="0"
            
        #print(len(possibleGenerator))
        for pos in range(len(possibleGenerator)):
            
            if possibleGenerator[pos][bit]==mx :
                generator.append(possibleGenerator[pos])
                #print(possibleGenerator[pos][bit],mx)
        for pos in range(len(possibleScrubber)):
            if possibleScrubber[pos][bit]==mini:
                scrubber.append(possibleScrubber[pos] )
        print(generator)       
        if len(generator)>=1:
            possibleGenerator=generator
        if len(scrubber)>=1:
            possibleScrubber=scrubber
            
    print(possibleGenerator, int(possibleGenerator[0],2)*int(possibleScrubber[0],2),possibleScrubber, "scru")
            
       
    #print(int(gama,2),int(delta,2))
part2()
#4182738
