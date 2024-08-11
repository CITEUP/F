grid = [input().strip() for _ in range(4)]
ada_solusi: bool = False
for i in range(3):
    if ada_solusi:
        break
    for j in range(3):
        subgrid = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
        hash_count = subgrid.count('#')
        dot_count = subgrid.count('.')
        if hash_count >= 3 or dot_count >= 3:
            print("YES")
            ada_solusi = True
            break
if not ada_solusi:
    print("NO")