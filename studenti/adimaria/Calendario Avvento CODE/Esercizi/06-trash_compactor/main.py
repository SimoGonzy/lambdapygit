'''
Soluzione per Exercise 6: Trash Compactor
Goal: Sum of results of vertical math problems.
'''

from parser import parse_exercise

def solve_problem(tokens):
    # Tokens list like ['123', '45', '6', '*'] or ['328', '64', '98', '+']
    # Last token should be operator (or one of them is operator)
    # Basic heuristic: last item is operator, rest are numbers.
    # Check if last item is op
    if not tokens:
        return 0
        
    op = tokens[-1]
    numbers = [int(x) for x in tokens[:-1]]
    
    if op == '+':
        return sum(numbers)
    elif op == '*':
        res = 1
        for n in numbers:
            res *= n
        return res
    else:
        # Fallback or error?
        # Maybe operator is distinct?
        print(f"Unknown operator: {op}")
        return 0

def main():
    lines = parse_exercise("./demo.txt")
    if not lines:
        print("Total: 0")
        return
        
    # Pad lines to max length
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    # Identify column groups
    # A group is separated by one or more empty columns (all spaces)
    
    groups_tokens = []
    
    current_col_start = 0
    in_problem = False
    
    # Iterate columns
    # We want to slice columns [start:end] that contain non-spaces
    
    # Simpler approach:
    # Scan columns. If column has ANY non-space, it's part of a problem.
    # If column is ALL spaces, it's a separator.
    
    problem_cols = []
    
    for c in range(max_len):
        col_chars = [line[c] for line in padded_lines]
        is_empty = all(char == ' ' for char in col_chars)
        
        if not is_empty:
            if not in_problem:
                in_problem = True
                current_col_start = c
        else:
            if in_problem:
                in_problem = False
                # End of a problem block
                problem_cols.append((current_col_start, c))
                
    # Handle last block if extends to edge
    if in_problem:
        problem_cols.append((current_col_start, max_len))
        
    total_sum = 0
    
    for start, end in problem_cols:
        # Extract parsing block
        block_tokens = []
        # We read the block row by row, or just extract all tokens?
        # "Each problem's numbers are arranged vertically"
        # "123" could be aligned right or left.
        # "The left/right alignment ... can be ignored."
        # So we just need to get all text in this vertical strip and split by whitespace.
        
        text_content = ""
        for line in padded_lines:
            text_content += line[start:end] + " "
            
        # Split by whitespace to get tokens
        tokens = text_content.split()
        
        # Solve
        result = solve_problem(tokens)
        total_sum += result
        
    print(f"Grand total: {total_sum}")

if __name__ == "__main__":
    main()
