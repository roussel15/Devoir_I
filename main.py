# main.py
from maze import Maze
from dfs import dfs
from bfs import bfs
from astar import astar

def print_path(path):
    if path is None:
        print("Chemin : Aucun chemin trouvé")
        return
    formatted = []
    for i, (x, y) in enumerate(path):
        if i == 0:
            formatted.append(f"S({x},{y})")
        elif i == len(path)-1:
            formatted.append(f"G({x},{y})")
        else:
            formatted.append(f"({x},{y})")
    print("Chemin :", " -> ".join(formatted))

def run_algorithm(name, algo, original_maze):
    print(f"\n===== {name} =====")
    maze = original_maze.copy()
    result = algo(maze)

    # Exploration (désactivée pour A*)
    if name != "A*":
        print("\nExploration :")
        maze_explore = original_maze.copy()
        maze_explore.mark_explored(result["explored"])
        maze_explore.display()


    # Solution
    print("\nSolution :")
    maze_solution = original_maze.copy()
    maze_solution.mark_path(result["path"])
    maze_solution.display()

    # Chemin
    print()
    print_path(result["path"])

    # Stats
    print("\nStatistiques :")
    print("Noeuds explorés :", result["nodes"])
    print("Longueur du chemin :", result["length"])
    print("Temps d'exécution : {:.6f} secondes".format(result["time"]))

def main():
    maze = Maze()
    print("Labyrinthe initial :\n")
    maze.display()

    results = []

    # Exécuter chaque algo UNE SEULE FOIS
    for name, algo in [("DFS", dfs), ("BFS", bfs), ("A*", astar)]:
        print(f"\n===== {name} =====")
        maze_copy = maze.copy()
        result = algo(maze_copy)

        # Affichage exploration
        print("\nExploration :")
        maze_explore = maze.copy()
        maze_explore.mark_explored(result["explored"])
        maze_explore.display()

        # Affichage solution
        print("\nSolution :")
        maze_solution = maze.copy()
        maze_solution.mark_path(result["path"])
        maze_solution.display()

        # Chemin
        print()
        print_path(result["path"])

        # Statistiques
        print("\nStatistiques :")
        print("Noeuds explorés :", result["nodes"])
        print("Longueur du chemin :", result["length"])
        print("Temps d'exécution : {:.6f} secondes".format(result["time"] / 1000))

        # Sauvegarder pour le tableau final
        results.append((name, result))

    # Afficher le tableau comparatif
    print("\n\n===== COMPARAISON =====")
    print(f"{'Algorithme':15} {'Noeuds':8} {'Longueur':10} {'Temps (ms)':10}")
    print("-" * 55)

    for name, r in results:
        print(f"{name:15} {r['nodes']:<8} {r['length']:<10} {r['time']:<10.3f}")


if __name__ == "__main__":
    main()
