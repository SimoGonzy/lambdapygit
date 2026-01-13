from pathlib import Path

def parse_exercise(input_file: str) -> list[tuple[int, int]]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    content = input_file_path.read_text().splitlines()
    
    # Input is single line or multi line?
    # Example:
    # 7,1 11,1 11,7 9,7 9,5 2,5 2,3 7,3
    # Wait, the example block shows:
    # 7,1 11,1 11,7 9,7 9,5 2,5 2,3 7,3
    # It might be space separated on one line? 
    # Or newline separated?
    # "They even have a list of where the red tiles are located... For example: ... 7,1 11,1 ... "
    # Most AoC inputs are newline separated, but this example shows one line.
    # However, "This list describes the position of 20 junction boxes, one per line" was for Day 8.
    # For Day 9: "For example: 7,1 11,1 ... 7,3"
    # It looks like a sequence.
    # I will support both space/newline separation to be safe.
    
    tile_strings = input_file_path.read_text().replace('\n', ' ').split()
    points = []
    for s in tile_strings:
        parts = s.split(',')
        if len(parts) == 2:
            points.append((int(parts[0]), int(parts[1])))
            
    return points
