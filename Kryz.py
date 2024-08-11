n=4
m=4
list=[]
for x in range(n) : 
    s=input()
    list.append(s)
ok=0
for x in range(3): 
    for y in range (3):
        ans=0
        if list[x][y]=='.' : ans+=1
        if list[x+1][y]=='.': ans+=1
        if list[x][y+1]=='.':ans+=1
        if list[x+1][y+1]=='.':ans+=1
        if ans==3 or ans==1 or ans==0 or ans==4 : ok=1
    
 
if ok==1 : print("YES")
else : print("NO")