from pathlib import Path

def parse_exercise(input_file: str) -> list[tuple[int, int, int]]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    content = input_file_path.read_text().splitlines()
    
    points = []
    for line in content:
        x, y, z = map(int, line.split(','))
        points.append((x, y, z))
        
    return points
