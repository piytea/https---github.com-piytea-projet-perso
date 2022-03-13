total=[]
solution=[]
nbsol=0
with open('input.txt','r',encoding='utf-8') as f:
    for code in f.readlines():
        total.append(code)
def jeu():
    n=0
    for l in total:
        
        
        liste=l.split(" ")
        nbletre=liste[0].split("-")
        letre=liste[1][:-1]
        code=liste[2]
        
        if letre in code:
            if code.count(letre)>=int(nbletre[0])and code.count(letre)<=int(nbletre[1]):
                solution.append(l)
                n+=1
                
    return n
def jeu2():
    n=0
        
    for l in total:
        liste=l.split(" ")
        nbletre=liste[0].split("-")
        letre=liste[1][:-1]
        code=liste[2]
        
        if letre in code:
            le=[]
            if list(code)[int(nbletre[0])-1]==letre and list(code)[int(nbletre[1])-1]!=letre:
                solution.append(l)
                n+=1
            if list(code)[int(nbletre[0])-1]!=letre and list(code)[int(nbletre[1])-1]==letre:
                solution.append(l)
                n+=1
                
    return n,solution
print(jeu2())

