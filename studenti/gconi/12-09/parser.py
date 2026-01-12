from pathlib import Path
from typing import TypedDict


class ExerciseInput(TypedDict):
    direzione: str
    valore: int


def parse_exercise(input_file: str) -> list[ExerciseInput]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    file_contents: str = input_file_path.read_text()
    contents_lines: list[str] = file_contents.splitlines()

    return list(
        map(
            lambda line: {"direzione": line[0], "valore": int(line[1:])}, contents_lines
        )
    )
