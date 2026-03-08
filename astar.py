# astar.py
import time
import heapq

def astar(maze):
    start = maze.get_start()
    goal = maze.get_goal()
    start_time = time.perf_counter()

    open_set = [(0, start)]
    g = {start: 0}
    parent = {}
    closed = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            break

        for n in maze.neighbors(current):
            tentative = g[current] + 1
            if n not in g or tentative < g[n]:
                g[n] = tentative
                f = tentative + manhattan(n, goal)
                heapq.heappush(open_set, (f, n))
                parent[n] = current

    end_time = time.perf_counter()
    path = reconstruct_path(parent, start, goal)

    return {
        "path": path,
        "explored": closed,
        "nodes": len(closed),
        "length": len(path) if path else 0,
        "time": (end_time - start_time) * 1000
    }

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return None
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return list(reversed(path))
