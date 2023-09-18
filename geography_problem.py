from collections import deque

def find_word_chain(original_list_of_words, search_method):
    
    def solve_geograpgy_problem_using_bfs(queue, recursion_depth):
        while queue:
            current_word, current_sequence = queue.popleft()
            recursion_depth += 1
            
            last_letter = current_word[-1]
            match_list = graph_of_first_letter.get(last_letter)
            
            # If there are no words starting with the last letter, return None
            if match_list is None:
                continue
            
            steps = 0
            for word in match_list:
                steps += 1
                # Print the state (word) as it is visited
                current_sequence_d = ', '.join(current_sequence)
                print("Recursion depth: {depth}, steps: {steps}, current sequence: {current_sequence} and visiting {word}".format(
                    depth=recursion_depth,
                    steps=steps,
                    current_sequence=current_sequence_d,
                    word=word,
                ))

                # uses current_sequence as used_word/visited_word as word can exist once.
                if word not in current_sequence:
                    new_sequence = current_sequence + [word]
                    if len(new_sequence) == len(original_list_of_words):
                        return new_sequence
                    
                    queue.append((word, new_sequence))
        
        return None  # No valid sequence found

    # Depth-first search function to find a word chain
    def solve_geograpgy_problem_using_dfs(word, stack, recursion_depth):
        if len(stack) == len(original_list_of_words):
            return stack

        last_letter = word[-1]
        match_list = graph_of_first_letter.get(last_letter)
        # If there are no words starting with the last letter, return None
        if match_list is None:
            return None
        
        recursion_depth += 1
        steps = 0
        for next_word in match_list:

            steps += 1
            # Print the state (word) as it is visited
            current_sequence_d = ', '.join(stack)
            print("Recursion depth: {depth}, steps: {steps}, current sequence: {current_sequence} and visiting {word}".format(
                depth=recursion_depth,
                steps=steps,
                current_sequence=current_sequence_d,
                word=next_word,
            ))

            # used stack as used_word/visited_word as word can exist once.            
            if next_word not in stack:
                stack.append(next_word)
                
                # Recursively search for the next word in the chain
                result = solve_geograpgy_problem_using_dfs(next_word, stack, recursion_depth)
                if result:
                    return result
                
                # Backtrack by removing the current word
                stack.pop()
    
    initial_word = original_list_of_words[0]
    
    original_list_of_words = set(original_list_of_words)
    if len(original_list_of_words) == 1:
        return initial_word
    
    # Create a graph_of_first_letter where each word is a node with outgoing edges to words that start with its last letter
    graph_of_first_letter = {}
    for word in original_list_of_words:
        if word[0] not in graph_of_first_letter:
            graph_of_first_letter[word[0]] = []
        graph_of_first_letter[word[0]].append(word)
        
    recursion_depth = 0
    
    if search_method == 'BFS':
        queue = deque([(initial_word, [initial_word,])])
        return solve_geograpgy_problem_using_bfs(queue, recursion_depth)
        
    elif search_method == 'DFS':
        stack = [initial_word,]
        return solve_geograpgy_problem_using_dfs(initial_word, stack, recursion_depth)

if __name__ == '__main__':
    # Example list_of_words to form a word chain
    list_of_words = ["ABC", "CDE", "CFG", "EHE", "EIJ", "GHK", "GLC"]
    # list_of_words = ["apple", "lion", "nut", "elephant", "tiger", 'redpoll', 'apple']
    
    print("Please enter a list of words separated by commas, or press Enter to use the default value.")
    user_input_words = input("Value: ").strip().upper()
    if user_input_words:
        user_input_words = user_input_words.replace('.', '')
        user_input_words = user_input_words.split(',')

        if len(user_input_words) == 1:
            raise ValueError('The input should contain more than one word separated by commas.') 
        
        list_of_words = [word.strip() for word in user_input_words]

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
