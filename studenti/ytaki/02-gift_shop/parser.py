from pathlib import Path


def parse_exercise(input_file: str) -> list[tuple[int, int]]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    file_contents: str = input_file_path.read_text()
    contents_lines: list[str] = file_contents.split(",")

    return list(map(
        lambda couple: (int(couple[0]), int(couple[1])),
        map(
            lambda line: line.split("-"),
            contents_lines
        )
    ))
