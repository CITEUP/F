strarr = [(input()) for i in range(4)]
direx = [(0,0),(-1,0),(0,1),(1,1)]
ans = False
for i in range(3):
    for j in range(3):
        black,white =0,0
        for a,b in direx:
            if(strarr[i+a][j+b] == "#"):
                black+=1
            elif(strarr[i+a][j+b] == "."):
                white+=1
        
        if(black > white or white > black):
            ans = True
            break
    if(ans):
        break
print("YES" if ans else "NO")