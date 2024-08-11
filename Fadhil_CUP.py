def iq_test(grid):
    for i in range:
        for j in range(3):
            cells = [
                grid[i][j], grid[i][j + 1],
                grid[i + 1][j], grid[i + 1][j]
            ]
            count_white = cells.count('.')
            count_black = celss.count('#')
            
            if count_white >= 3 or count_black >= 3:
                return "YES"
    return "NO"
    
grid = [input().strip() for _ in range(4)]
print(iq_test(grid))