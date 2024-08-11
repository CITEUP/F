def test(square):
    for i in range(3):
        for j in range(3):
            if square[i][j] == square[i][j + 1] == square[i + 1][j] == square[i + 1][j + 1]:
                return "YES"
    for i in range(4):
        for j in range(4):
            square[i][j] = "#" if square[i][j] == "." else "."
            for x in range(3):
                for y in range(3):
                    if square[x][y] == square[x][y + 1] == square[x + 1][y] == square[x + 1][y + 1]:
                        return "YES"
            square[i][j] = "#" if square[i][j] == "." else "."
    return "NO"
square = [list(input()) for _ in range(4)]
print(test(square))