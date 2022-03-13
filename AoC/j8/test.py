input = open("test.txt", "r")
data = []

for line in input:
    data += [line.strip().split()]

visited = [False for i in range(len(data))]
accumulator = 0
index = 0
while not visited[index]:
    visited[index] = True
    if data[index][0] == 'acc':
        accumulator += int(data[index][1])
        index+=1
    elif data[index][0] == 'jmp':
        index += int(data[index][1])
    elif data[index][0] == 'nop':
        index += 1
print(accumulator)
