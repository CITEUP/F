p=[]
for i in range(4):
    p.append(input())
a="NO"
for row in range(0, 3):
    for column in range(0, 3):
        if p[row][column:column+2].count("#")+p[row+1][column:column+2].count("#") > 2:
            a="YES"
            break
    if a=="YES":
        break
print(a)