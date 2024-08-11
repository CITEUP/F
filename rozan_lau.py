
s = ["", "", "", ""]
for i in range(0, 4):
    s[i] = input()

mn = 10

for i in range(1, 4):
    for j in range(1, 4):
        cnt = 0
        for x in range(i - 1, i + 1):
            for y in range(j - 1, j + 1):
                if s[x][y] == '.':
                    cnt += 1
        mn = min(mn, min(cnt, 4 - cnt))

if mn <= 1:
    print("YES")
else:
    print("NO")
