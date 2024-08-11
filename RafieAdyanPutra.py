def can_pass_test(grid):
    def is_uniform(cells):
        return len(set(cells)) == 1
        
    for i in range(3):
        for j in range(3):
            cells = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
            
            if is_uniform(cells):
                return "YES"
                
            counts = {color: cells.count(color) for color in set(cells)}
            
            if max(counts.values()) >= 3:
                return "YES"
            else:
                return "NO"

grid = [input().strip() for _ in range(4)]

print(can_pass_test(grid))