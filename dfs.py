# dfs.py
import time

def dfs(maze):
    start = maze.get_start()
    goal = maze.get_goal()
    start_time = time.perf_counter()

    stack = [start]
    visited = set()
    parent = {}

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for n in maze.neighbors(current):
            if n not in visited:
                parent[n] = current
                stack.append(n)

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
