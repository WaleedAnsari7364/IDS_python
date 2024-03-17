ACTIONS = [(0, 1, 2), (1, 0, 2), (1, 1, 3)] 
def read_maze(filename):
    with open(filename, 'r') as file:
        rows, cols = map(int, file.readline().split())
        start = tuple(map(int, file.readline().split()))
        goal = tuple(map(int, file.readline().split()))
        maze = [list(map(int, line.strip())) for line in file]
    return rows, cols, start, goal, maze

def is_valid_move(rows, cols, maze, row, col):
    return 0 <= row < rows and 0 <= col < cols and maze[rows-row-1][col] == 0

def ids(start, goal, maze, max_depth):
    rows = len(maze)
    cols = len(maze[0])
    stack = [(start, [start], 0)]
    
    while stack:
        current_pos, path, cost = stack.pop()
        
        if current_pos == goal:
            return path, cost
        
        if len(path) < max_depth:
            for dr, dc, move_cost in ACTIONS:
                new_row, new_col = current_pos[0] + dr, current_pos[1] + dc
                new_pos = (new_row, new_col)
                new_cost = cost + move_cost
                if is_valid_move(rows, cols, maze, new_row, new_col) and new_pos not in path:
                    new_path = path + [new_pos]
                    stack.append((new_pos, new_path, new_cost))
    
    return None, None

def display_path(rows, cols, maze, path):
    for r in range(rows):
        for c in range(cols):
            if (rows - r - 1, c) in path:
                print('*', end=' ')
            else:
                print(maze[r ][c], end=' ')
        print()


#MAIN
filename=input("Enter Filename: ")
rows, cols, start, goal, maze = read_maze(filename)
print("Rows:", rows)
print("Cols:", cols)
print("Start coordinates:", start)
print("Goal coordinates:", goal)
print("Maze:")
for i in maze:
    print(i)


found_path = None
min_cost = float('inf')
max_depth = 1
while max_depth <= rows * cols:
    found_path, cost = ids(start, goal, maze, max_depth)
    if found_path and cost < min_cost:
        min_cost = cost
    max_depth += 1

if found_path:
    print("Minimum cost:", min_cost)
    print("Path found:")
    print(found_path)
    display_path(rows,cols,maze,found_path)
else:
    print("No path found.")
