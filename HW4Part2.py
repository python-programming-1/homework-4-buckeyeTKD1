grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
n=0
while n<6: 
        print (grid[0][int(n)],grid[1][int(n)],grid[2][int(n)],grid[3][int(n)],grid[4][int(n)],grid[5][int(n)],grid[6][int(n)],grid[7][int(n)],grid[8][n])
        n=n+1
else: 	
        print("bye") 
