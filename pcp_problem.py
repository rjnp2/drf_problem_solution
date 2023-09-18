from collections import deque

def match_top_bottom_domino(dominos, search_method):
    
    def solve_pcp_problem_using_bfs(queue, recursion_depth, steps):
        # print(queue)
        while queue:
            current_path = queue.popleft()
            recursion_depth += 1
            
            for path in current_path:
                for domino in dominos:
                    steps += 1
                    
                    print("Recursion depth: {depth}, steps: {steps} and visting: {paths}".format(
                        depth=recursion_depth,
                        paths=domino,
                        steps=steps
                    ))
                    
                    new_path = path.copy()
                    new_path.append(domino)
                    
                    top_domino = "".join([d[0] for d in new_path])
                    bottom_domino = "".join([d[1] for d in new_path])
                    
                    # Check if top and bottom are equal
                    if top_domino == bottom_domino:
                        return [top_domino, bottom_domino]

                    # Check for partial match and add to new_possible_paths
                    min_len = min(len(top_domino), len(bottom_domino))
                    if top_domino[:min_len] == bottom_domino[:min_len]:
                        queue.append([new_path,])
        
    def solve_pcp_problem_using_dfs(all_possible_paths, recursion_depth, steps):
        # Base case: If there are no more paths to explore, return None
        if not all_possible_paths:
            return None
        
        new_possible_paths = []
        recursion_depth += 1
        for path in all_possible_paths:
            for domino in dominos:
                new_path = path.copy()
                new_path.append(domino)
                
                steps += 1
                
                print("Recursion depth: {depth}, steps: {steps} and visting: {paths}".format(
                    depth=recursion_depth,
                    paths=domino,
                    steps=steps
                ))
                
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
        
        # Continue the search with new_possible_paths
        return solve_pcp_problem_using_dfs(new_possible_paths, recursion_depth, steps)
    
    if len(dominos) == 1:
        return None 
    
    recursion_depth = 0
    steps = 0
    
    # Initialize all_possible_paths with dominoes having an initial partial match
    all_possible_paths = []
    for domino in dominos:
        top_domino, bottom_domino = domino
        min_len = min(len(top_domino), len(bottom_domino))
        
        if top_domino[:min_len] == bottom_domino[:min_len]:
            all_possible_paths.append([domino,])
    
    if search_method == 'BFS':
        queue = deque([all_possible_paths, ])
        return solve_pcp_problem_using_bfs(queue, recursion_depth, steps)
        
    elif search_method == 'DFS':
        return solve_pcp_problem_using_dfs(all_possible_paths, recursion_depth, steps)

if __name__ == '__main__':
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

    # dominoes = [
    #     ('AA', 'A')
    # ]

    print("Please enter dominoes separated by a single space for the top and bottom of the same domino and separated by commas for different dominoes,")
    print("or press Enter to use the default value.")
    print(f"Example: bba b, ba baa for ('bba', 'b'), ('ba', 'baa')")
    user_input_words = input("Value: ").strip().upper()
    if user_input_words:
        user_input_words = user_input_words.replace('.', '').split(',')
        dominoes = []

        if len(user_input_words) <= 1:
            raise ValueError('The input should contain more than one word separated by commas.') 
        
        for inner_list in user_input_words:
            inner_list = inner_list.strip().split(' ')

            if len(inner_list) != 2:
                raise ValueError('Each individual domino should have a length of 2.') 
            
            domino = [ele.strip() for ele in inner_list]
            dominoes.append(domino)

    while True:
        search_method = input("Choose BFS or DFS (Enter 'BFS' or 'DFS'): ").strip().upper()
        if search_method in ['BFS', 'DFS']:
            break

    # Find a solution for the PCP problem
    solution = match_top_bottom_domino(dominoes, search_method)

    if solution:
        print(f"Match found: {solution[0]} domino top is equal to {solution[1]} domino bottom with a size of {len(solution[0])} each.")
    else:
        print("No match found.")
