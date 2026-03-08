# maze.py
import random
import copy
from collections import deque

SIZE = 16
SEED = 42

class Maze:
    def __init__(self):
        random.seed(SEED)
        self.grid = self._generate()

    def _generate(self):
        while True:
            # Grille pleine de murs
            grid = [['#' for _ in range(SIZE)] for _ in range(SIZE)]

            # Positions internes (sans bordures)
            internal = [(i, j) for i in range(1, SIZE-1)
                                 for j in range(1, SIZE-1)]

            # Retirer S et G
            internal.remove((1,1))
            internal.remove((SIZE-2,SIZE-2))

            # Nombre de murs ≈ 35 % de la surface interne (hors S et G)
            walls_needed = int(len(internal) * 0.35)

            wall_positions = set(random.sample(internal, walls_needed))

            # Remplissage
            for (i, j) in internal:
                grid[i][j] = '#' if (i,j) in wall_positions else '.'

            # Placer S et G
            grid[1][1] = 'S'
            grid[SIZE-2][SIZE-2] = 'G'

            # Vérifier qu'un chemin existe avec BFS simple
            if self._path_exists(grid):
                return grid

    def _path_exists(self, grid):
        start = (1,1)
        goal = (SIZE-2, SIZE-2)
        queue = deque([start])
        visited = set([start])

        while queue:
            x, y = queue.popleft()
            if (x,y) == goal:
                return True
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < SIZE and 0 <= ny < SIZE:
                    if grid[nx][ny] in ('.','G') and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
        return False

    def copy(self):
        new_maze = Maze()
        new_maze.grid = copy.deepcopy(self.grid)
        return new_maze

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def mark_explored(self, explored):
        for (x, y) in explored:
            if self.grid[x][y] == '.':
                self.grid[x][y] = 'p'

    def mark_path(self, path):
        if path is None:
            return
        for (x, y) in path:
            if self.grid[x][y] == '.':
                self.grid[x][y] = '*'

    def get_start(self):
        return (1,1)

    def get_goal(self):
        return (SIZE-2,SIZE-2)

    def is_walkable(self, pos):
        x, y = pos
        return self.grid[x][y] in ('.','S','G')


    def in_bounds(self, pos):
                   x, y = pos
                   return 0 <= x < SIZE and 0 <= y < SIZE

    def neighbors(self, pos):
                  x, y = pos
                  dirs = [(0,1),(1,0),(0,-1),(-1,0)]
                  for dx, dy in dirs:
                              nx, ny = x+dx, y+dy
                              if self.in_bounds((nx,ny)) and self.is_walkable((nx,ny)):
                                        yield (nx,ny)

