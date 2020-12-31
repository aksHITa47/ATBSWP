def pic(grids):
    for j in range(6):
        for i in range(len(grids)):
            print(grids[i][j],end='')
        print()
            
grid = [[' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'O', 'O', ' ', ' ', ' '],
        ['O', 'O', 'O', 'O', ' ', ' '],
        ['O', 'O', 'O', 'O', 'O', ' '],
        [' ', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', ' '],
        ['O', 'O', 'O', 'O', ' ', ' '],
        [' ', 'O', 'O', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ']]
pic(grid)

# It's a heart UwU!