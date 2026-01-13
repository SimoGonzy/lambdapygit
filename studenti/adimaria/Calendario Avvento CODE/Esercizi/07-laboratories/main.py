'''
Soluzione per Exercise 7: Laboratories
Goal: Count total tachyon beam splits.
'''

from parser import parse_exercise

def main():
    grid = parse_exercise("./demo.txt")
    
    rows = len(grid)
    cols = len(grid[0])
    
    # 1. Find Start 'S'
    active_beams = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                active_beams.add((r, c))
                break
    
    split_count = 0
    
    # Loop until no beams are left
    while active_beams:
        next_beams = set()
        
        for r, c in active_beams:
            # Move beam down
            nr, nc = r + 1, c
            
            # Check bounds
            if nr >= rows:
                continue
                
            cell = grid[nr][nc]
            
            if cell == '^':
                split_count += 1
                # Split: Left and Right
                # "from the immediate left and from the immediate right of the splitter"
                # The text says "a new tachyon beam continues from the immediate left and from the immediate right"
                # This implies the new beams start at (nr, nc-1) and (nr, nc+1)?
                # Let's check the example.
                # S at row 0.
                # | at row 1.
                # ^ at row 2.
                # New beams at row 2, col left and row 2, col right?
                # Example visual:
                # ......|^|......
                # The beams are ON the same row as the splitter?
                # "instead, a new tachyon beam continues from the immediate left and from the immediate right"
                # So if ^ is at (r,c), new beams are at (r, c-1) and (r, c+1).
                
                # Check bounds for new beams and add if valid
                if 0 <= nc - 1 < cols:
                    next_beams.add((nr, nc - 1))
                if 0 <= nc + 1 < cols:
                    next_beams.add((nr, nc + 1))
                    
            else: # '.' or '|' or anything else that passes through
                # Check if it's not a splitter.
                # Wait, does the beam stop if it hits something else?
                # "Tachyon beams pass freely through empty space (.)"
                # The example shows pipes '|' being drawn, but they are just history trails.
                # Input only has S, ., ^.
                # So anything not ^ is pass through.
                next_beams.add((nr, nc))
        
        active_beams = next_beams
        
    print(f"Total splits: {split_count}")

if __name__ == "__main__":
    main()
