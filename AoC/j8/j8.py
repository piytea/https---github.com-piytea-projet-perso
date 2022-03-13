com=[]
with open('input.txt','r',encoding='utf-8') as f:
    for ligne in f.readlines():
        com.append((ligne[:-1].split(" ")))

def jeu(com):
    visite=[False for i in range(len(com))]
    total=0
    val=0
    while 0 <= val < len(com) and not visite[val]:       
        visite[val]=True
        if com[val][0]=="acc":
            total+=int(com[val][1])
            val+=1
        elif com[val][0]=="jmp":
            val+=int(com[val][1]) 
        elif com[val][0]=="nop":
            val+=1
        
    
    return total if val== len(com) else None
def swap(op):
    if op == 'jmp':
        return 'nop'
    if op == 'nop':
        return 'jmp'
    return op

def test(com):
    for i in range(len(com)):
        com[i][0] = swap(com[i][0])
        out = jeu(com)
        com[i][0] = swap(com[i][0])
        if(out is not None):
            return out
    return None

print(test(com))
            
