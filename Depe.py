def solve():
    grid = [[] for _ in range(4)];
    
    for i in range(4):
        grid[i] = input();
    
    for i in range(3):
        for j in range(3):
            cnt = 0;
            if (grid[i][j] == "."): cnt += 1;
            if (grid[i+1][j] == "."): cnt += 1;
            if (grid[i][j+1] == "."): cnt += 1;
            if (grid[i+1][j+1] == "."): cnt += 1;
            
            if (cnt != 2):
                print("YES");
                return;
                
    print("NO");

t = 1;
#t = int(input());
for i in range(t):
    solve();