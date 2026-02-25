'''
Soluzione per Exercise 10: Factory
Goal: Sum of fewest button presses to configure all machines.
Each button toggles specific lights.
'''

from parser import parse_exercise
import itertools

def solve_machine(machine):
    initial = machine["initial_lights"]
    buttons = machine["buttons"]
    num_lights = len(initial)
    num_buttons = len(buttons)
    
    # Target state: We want to find combination of buttons such that
    # Final state is ALL lights ... wait.
    # Problem: "simultaneously configure the first light to be off, the second light to be on..."
    # "So, an indicator light diagram like [.##.] means that... the goal is to simultaneously configure the first light to be off..."
    # Wait, the diagram IS the goal?
    # "To start a machine, its indicator lights must match those shown in the diagram"
    # "The machine has the number of indicator lights shown, but its indicator lights are all initially off."
    # YES. Initial state is all 0. Goal is `initial` (parsed from diagram).
    
    # We want XOR sum of button actions to equal goal.
    # Convert goal to integer mask?
    
    target_mask = 0
    for i, val in enumerate(initial):
        if val:
            target_mask |= (1 << i)
            
    button_masks = []
    for b_indices in buttons:
        mask = 0
        for idx in b_indices:
            mask |= (1 << idx)
        button_masks.append(mask)
        
    # Brute force 2^num_buttons
    # Num buttons seems small in example (6, 5, 4).
    # Assuming input also has small number of buttons (< 20).
    
    min_presses = float('inf')
    found = False
    
    for i in range(1 << num_buttons):
        # Calculate effect of this combination
        current_mask = 0
        press_count = 0
        
        for b in range(num_buttons):
            if (i >> b) & 1:
                current_mask ^= button_masks[b]
                press_count += 1
                
        if current_mask == target_mask:
            found = True
            if press_count < min_presses:
                min_presses = press_count
                
    if found:
        return min_presses
    else:
        # Should not happen based on problem
        return 0

def main():
    machines = parse_exercise("./demo.txt")
    
    total_min_presses = 0
    
    for machine in machines:
        presses = solve_machine(machine)
        total_min_presses += presses
        
    print(f"Total min presses: {total_min_presses}")

if __name__ == "__main__":
    main()
