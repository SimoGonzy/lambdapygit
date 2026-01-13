from pathlib import Path
import re

def parse_exercise(input_file: str) -> list[dict]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    lines = input_file_path.read_text().splitlines()
    
    machines = []
    for line in lines:
        if not line.strip():
            continue
            
        # Parse Diagram: [.##.]
        diagram_match = re.search(r'\[([.#]+)\]', line)
        if not diagram_match:
            continue
        diagram_str = diagram_match.group(1)
        # Convert to boolean list or binary mask
        # Length could vary? Yes.
        initial_lights = [1 if c == '#' else 0 for c in diagram_str]
        
        # Parse buttons: (0,3,4) or (3)
        # \(([\d,]+)\)
        buttons_raw = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        for b_str in buttons_raw:
            indices = [int(x) for x in b_str.split(',')]
            buttons.append(indices)
            
        # Joltage requirements {3,5,4,7} - irrelevant
        
        machines.append({
            "initial_lights": initial_lights,
            "buttons": buttons
        })
        
    return machines
