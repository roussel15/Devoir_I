# bfs.py
import time
from collections import deque

def bfs(maze):
    start = maze.get_start()
    goal = maze.get_goal()
    start_time = time.perf_counter()

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        for n in maze.neighbors(current):
            if n not in visited:
                visited.add(n)
                parent[n] = current
                queue.append(n)

    end_time = time.perf_counter()
    path = reconstruct_path(parent, start, goal)

    return {
        "path": path,
        "explored": visited,
        "nodes": len(visited),
        "length": len(path) if path else 0,
        "time": (end_time - start_time) * 1000
    }

def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return None
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return list(reversed(path))
