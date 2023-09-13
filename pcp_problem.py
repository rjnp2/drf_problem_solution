def match_top_bottom_domino(dominos):
    
    def solve_pcp_problem_using_dfs(all_possible_paths, recursion_depth, steps):
        # Base case: If there are no more paths to explore, return None
        if not all_possible_paths:
            return None
        
        new_possible_paths = []
        for path in all_possible_paths:
            for domino in dominos:
                new_path = path.copy()
                new_path.append(domino)
                
                steps += 1
                
                # Print the state (word) as it is visited
                print(f"Visiting: {domino}")
                
                # Concatenate top and bottom of the dominoes in the path
                top_domino = "".join([d[0] for d in new_path])
                bottom_domino = "".join([d[1] for d in new_path])
                
                # Check if top and bottom are equal
                if top_domino == bottom_domino:
                    return [top_domino, bottom_domino]
                
                # Check for partial match and add to new_possible_paths
                min_len = min(len(top_domino), len(bottom_domino))
                if top_domino[:min_len] == bottom_domino[:min_len]:
                    new_possible_paths.append(new_path)
                    
        recursion_depth += 1
        print("Recursion depth: {depth}, paths: {paths}, steps: {steps}".format(
            depth=recursion_depth,
            paths=len(all_possible_paths),
            steps=steps
        ))
        
        # Continue the search with new_possible_paths
        return solve_pcp_problem_using_dfs(new_possible_paths, recursion_depth, steps)
    
    recursion_depth = 0
    steps = 0
    
    # Initialize all_possible_paths with dominoes having an initial partial match
    all_possible_paths = []
    for domino in dominos:
        top_domino, bottom_domino = domino
        min_len = min(len(top_domino), len(bottom_domino))
        
        if top_domino[:min_len] == bottom_domino[:min_len]:
            all_possible_paths.append([domino,])
    
    # Start solving the PCP problem using depth-first search
    solution = solve_pcp_problem_using_dfs(all_possible_paths, recursion_depth, steps)
    
    return solution

# Example dominoes
dominoes = [
    ("bba", "b"),
    ("ba", "baa"),
    ("ba", "aba"),
    ("ab", "bba"),
]

# dominoes = [
#     ("MOM", "M"),
#     ("O", "OMOMO"),
# ]

dominoes = [
    ('AA', 'A')
]
# Find a solution for the PCP problem
solution = match_top_bottom_domino(dominoes)

if solution:
    print(f"Match found: {solution[0]} domino top is equal to {solution[1]} domino bottom with a size of {len(solution[0])} each.")
else:
    print("No match found.")
