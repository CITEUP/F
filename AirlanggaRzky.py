
# brute forceee
row1 = input()
row2 = input()
row3 = input()
row4 = input()

# case 1
bisa = False
for i in range(len(row1)-1):
    if(row1[i] == row1[i+1]):
        if(row1[i] == row2[i] or row1[i] == row2[i+1]):
            bisa = True
            
#case 2
for i in range(len(row2)-1):
    if(row2[i] == row2[i+1]):
        if(row2[i] == row3[i] or row2[i] == row3[i+1]):
            bisa = True
            
for i in range(len(row2)-1):
    if(row2[i] == row2[i+1]):
        if(row2[i] == row1[i] or row2[i] == row1[i+1]):
            bisa = True
            
# case 3
for i in range(len(row3)-1):
    if(row3[i] == row3[i+1]):
        if(row3[i] == row4[i] or row3[i] == row4[i+1]):
            bisa = True

for i in range(len(row3)-1):
    if(row3[i] == row3[i+1]):
        if(row3[i] == row2[i] or row3[i] == row2[i+1]):
            bisa = True


#case 4

for i in range(len(row4)-1):
    if(row4[i] == row4[i+1]):
        if(row4[i] == row3[i] or row4[i] == row3[i+1]):
            bisa = True
            
if bisa : print("YES")
else : print("NO")
        
