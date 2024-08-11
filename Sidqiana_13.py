data_pagar=list()
for i in range(4):
    data_pagar.append(input())
ans=list()
for i in data_pagar:
    for j in range(len(i)):
        if i[j]!=i[j-1]:
            ans.append('YES')
            break
        else:
            ans.append('NO')
print(ans[-1])
    