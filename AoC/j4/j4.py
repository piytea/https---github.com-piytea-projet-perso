total=[]
carte=[]
with open('input.txt','r',encoding='utf-8') as f:
    for code in f.readlines():
        carte.append(list(code[:-1].split(" ")))
        if len(code)<=1:
            total.append(carte)
            carte=[]


def jeu():
    test=0
    pasbon=0
    p=0
    val=["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    for ligne in range(len(total)):
        final=[]
        total[ligne]=total[ligne][:-1]
        
    for elm in total:
        nelm=[]
        p+=1
        for souselm in elm:
            nelm.extend(souselm)
            
        final.append(nelm)
    bon=len(final)
    for pers in final:
        if val.Contains(pers):
            test+=1
    print(final)
    print(len(total),bon,pasbon,test)
    print(len(total)-pasbon,)
                
            
        
    
jeu()
