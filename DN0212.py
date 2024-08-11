arr = []
for i in range(4):
    arr.append(input())
con = 0
for i in range(3):
    temp = arr[i]
    temp2 = arr[i+1]
    for j in range(3) :
        cnt = 0
        if(temp[j] == ".") :
            cnt+=1
        if (temp[j+1] == ".") :
            cnt+=1
        if (temp2[j+1] == ".") :
            cnt+=1
        if (temp2[j] == ".") :
            cnt+=1
        if (cnt >= 3 or cnt <= 1) :
            con = 1
            #print(i, j, cnt)
if (con == 1) :
    print("YES")
else :
    print("NO")
            
        