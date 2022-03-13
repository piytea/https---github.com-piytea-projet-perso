with open('inputJ8.txt', 'r') as fichier:
    txt = fichier.readlines()

print(txt[:10])
output=[]
for i in range(len(txt)):
    
    txt[i]=txt[i].split("|")
    output.append(txt[i][1].split(" "))
print(txt[:10])
print(output[:10])
