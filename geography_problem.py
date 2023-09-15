from collections import deque

def find_word_chain(original_list_of_words, search_method):
    
    def solve_geograpgy_problem_using_bfs(queue, recursion_depth, steps):
        while queue:
            current_word, current_sequence = queue.popleft()
            
            if len(current_sequence) == len(original_list_of_words):
                return current_sequence
            
            recursion_depth += 1
            
            last_letter = current_word[-1]
            match_list = graph_of_first_letter.get(last_letter)
            
            # If there are no words starting with the last letter, return None
            if match_list is None:
                return None
            
            for word in match_list:
                steps += 1
                # Print the state (word) as it is visited
                print("Recursion depth: {depth}, steps: {steps} and visiting {word}".format(
                    depth=recursion_depth,
                    steps=steps,
                    word=word,
                ))
                    
                if word not in current_sequence:
                    new_sequence = current_sequence + [word]
                    queue.append((word, new_sequence))
        
        return None  # No valid sequence found

    # Depth-first search function to find a word chain
    def solve_geograpgy_problem_using_dfs(word, recursion_depth, steps):
        if len(word_chain) == len(original_list_of_words):
            return word_chain

        last_letter = word[-1]
        match_list = graph_of_first_letter.get(last_letter)
        # If there are no words starting with the last letter, return None
        if match_list is None:
            return None
        
        recursion_depth += 1
        
        for next_word in match_list:
            if next_word not in used_words:
                word_chain.append(next_word)
                used_words.add(next_word)
                
                steps += 1
                # Print the state (word) as it is visited
                print("Recursion depth: {depth}, steps: {steps} and visiting {word}".format(
                    depth=recursion_depth,
                    steps=steps,
                    word=next_word,
                ))
                
                # Recursively search for the next word in the chain
                result = solve_geograpgy_problem_using_dfs(next_word, recursion_depth, steps)
                if result:
                    return result
                
                # Backtrack by removing the current word
                word_chain.pop()
                used_words.remove(next_word)
    
    # Create a graph_of_first_letter where each word is a node with outgoing edges to words that start with its last letter
    graph_of_first_letter = {}
    for word in original_list_of_words:
        if word[0] not in graph_of_first_letter:
            graph_of_first_letter[word[0]] = []
        graph_of_first_letter[word[0]].append(word)
        
    initial_word = original_list_of_words[0]
    used_words = set([initial_word])
    word_chain = [initial_word]
    recursion_depth = 0
    steps = 0
    
    if search_method == 'BFS':
        queue = deque([(initial_word, word_chain)])
        return solve_geograpgy_problem_using_bfs(queue, recursion_depth, steps)
        
    elif search_method == 'DFS':
        return solve_geograpgy_problem_using_dfs(initial_word, recursion_depth, steps)

# Example list_of_words to form a word chain
list_of_words = ["ABC", "CDE", "CFG", "EHE", "EIJ", "GHK", "GLC"]
list_of_words = ["apple", "lion", "nut", "elephant", "tiger", 'redpoll']

while True:
    search_method = input("Choose BFS or DFS (Enter 'BFS' or 'DFS'): ").strip().upper()
    if search_method in ['BFS', 'DFS']:
        break

# Find and print the word sequence
sequence_of_chain_words = find_word_chain(list_of_words, search_method)

if sequence_of_chain_words:
    sequence_of_chain_words = ' -> '.join(sequence_of_chain_words)
    print(sequence_of_chain_words)
else:
    print("No valid word sequence found.")
