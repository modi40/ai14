class AOStar:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = dict(heuristics)
        self.solution_tree = {}

    def get_branch_cost(self, branch):
        total_cost = 0
        node_list = []
        for child_node, edge_weight in branch:
            total_cost += edge_weight + self.heuristics.get(child_node, 0)
            node_list.append(child_node)
        return total_cost, node_list

    def apply_ao_star(self, node):
        if node not in self.graph or not self.graph[node]:
            return self.heuristics.get(node, 0)
            
        branches = self.graph[node]
        min_cost = float('inf')
        best_nodes = []
        
        for branch in branches:
            cost, nodes = self.get_branch_cost(branch)
            if cost < min_cost:
                min_cost = cost
                best_nodes = nodes
                
        self.heuristics[node] = min_cost
        self.solution_tree[node] = best_nodes
        
        for child in best_nodes:
            self.apply_ao_star(child)
            
        updated_min = float('inf')
        for branch in branches:
            cost, nodes = self.get_branch_cost(branch)
            if cost < updated_min:
                updated_min = cost
                best_nodes = nodes
        self.heuristics[node] = updated_min
        self.solution_tree[node] = best_nodes
        
        return self.heuristics[node]

    def print_solution(self, node, prefix=""):
        children = self.solution_tree.get(node, [])
        if not children:
            print(f"{prefix}- {node} (Leaf, Cost = {self.heuristics.get(node, 0)})")
            return
        print(f"{prefix}+ {node} (Cost = {self.heuristics.get(node, 0)}) -> Children: {children}")
        for child in children:
            self.print_solution(child, prefix + "  ")

def main():
    and_or_graph = {
        'A': [
            [('B', 2)],
            [('C', 3)]
        ],
        'B': [
            [('D', 1), ('E', 4)]
        ],
        'C': [
            [('F', 2)],
            [('G', 5)]
        ],
        'D': [
            [('H', 2)],
            [('I', 3)]
        ],
        'E': [
            [('J', 1)]
        ],
        'F': [],
        'G': [],
        'H': [],
        'I': [],
        'J': []
    }
    
    heuristics = {
        'A': 10, 'B': 6, 'C': 4,
        'D': 3, 'E': 2, 'F': 0, 'G': 0,
        'H': 0, 'I': 0, 'J': 0
    }
    
    print("AO* Algorithm for AND-OR Graph Search")
    print(f"Root Node: A")
    solver = AOStar(and_or_graph, heuristics)
    optimal_cost = solver.apply_ao_star('A')
    
    print("-" * 50)
    print(f"Optimal Heuristic Cost at Root A: {optimal_cost}")
    print("Optimal Solution Graph Subtree:")
    solver.print_solution('A')

if __name__ == '__main__':
    main()
