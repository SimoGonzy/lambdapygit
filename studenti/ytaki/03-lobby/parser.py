from pathlib import Path


def parse_exercise(input_file: str) -> list[str]:
    input_file_path: Path = Path(__file__).parent.joinpath(input_file)
    file_contents: str = input_file_path.read_text()
    return file_contents.splitlines()
