# x=['carrot', '-1', 'R']

x= list(map(str,(input().split())))
print(x)

word=list(x[0])
move=int(x[1])
direction=x[2]

print(range(move))

if direction=='L' or direction=='l':
    if move>=0:
        for i in range(move):
            word.append(word.pop(0))
        print("".join(word))
    else:
        for i in range(-move):
            word.insert(0, word.pop())
        print("".join(word))

elif direction=='R' or direction=='r':
    if move>=0:
        for i in range(move):
            word.insert(0, word.pop())
        print("".join(word))
    else:
        for i in range(-move):
            word.append(word.pop(0))
        print("".join(word))





# else:
