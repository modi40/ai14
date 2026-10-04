def minimax(node, depth, is_maximizing, game_tree, leaf_scores):
    if node in leaf_scores:
        return leaf_scores[node]
        
    children = game_tree.get(node, [])
    if is_maximizing:
        best_val = float('-inf')
        for child in children:
            val = minimax(child, depth + 1, False, game_tree, leaf_scores)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = float('inf')
        for child in children:
            val = minimax(child, depth + 1, True, game_tree, leaf_scores)
            best_val = min(best_val, val)
        return best_val

def main():
    game_tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G']
    }
    
    leaf_scores = {
        'D': 3,
        'E': 5,
        'F': 2,
        'G': 9
    }
    
    print("Minimax Algorithm for Two-Player Game")
    print("Game Tree Structure:")
    print("  Root A (MAX) -> Children: B, C (MIN)")
    print("  Node B (MIN) -> Leaves: D = 3, E = 5")
    print("  Node C (MIN) -> Leaves: F = 2, G = 9")
    print("-" * 50)
    
    score_b = minimax('B', 1, False, game_tree, leaf_scores)
    score_c = minimax('C', 1, False, game_tree, leaf_scores)
    score_a = max(score_b, score_c)
    
    print(f"Evaluated Score at Node B (MIN): min(3, 5) = {score_b}")
    print(f"Evaluated Score at Node C (MIN): min(2, 9) = {score_c}")
    print(f"Optimal Value at Root A (MAX)  : max({score_b}, {score_c}) = {score_a}")
    
    best_move = 'B' if score_b > score_c else 'C'
    print(f"Optimal First Move for MAX Player: Node {best_move}")

if __name__ == '__main__':
    main()
