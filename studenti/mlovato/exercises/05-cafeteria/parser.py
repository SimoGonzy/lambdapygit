from pathlib import Path
from typing import TypedDict


class ExerciseInput(TypedDict):
    id_fresh: list[tuple[int, int]]
    ingredienti: list[int]

def parse_exercise(input_file: str) -> ExerciseInput:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    file_contents: str = input_file_path.read_text()
    contents_lines: list[str] = file_contents.splitlines()

    separator_pos: int = contents_lines.index("")
    id_fresh_lines: list[str] = contents_lines[:separator_pos]
    ingredienti_lines: list[str] = contents_lines[separator_pos + 1:]

    return {
        "id_fresh": [
            (int(line.split("-")[0]), int(line.split("-")[1])) for line in id_fresh_lines
        ],
        "ingredienti": [
            int(line) for line in ingredienti_lines
        ]
    }
