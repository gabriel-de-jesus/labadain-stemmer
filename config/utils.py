from pathlib import Path

#!/usr/bin/env python3
#
# config.utils.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# 09-05-2024

class Utils:
    """The utilities class for reading and writing files."""

    def __init__(self) -> None:
        pass

    def load_corpus(self, file_path: Path) -> str:
        """Load the given text file."""
        try:
            with file_path.open('r', encoding='utf-8') as f_corpus:
                corpus_contents = f_corpus.read()
        except FileNotFoundError:
            print(f"File not found at: {file_path}")
            return []

        return corpus_contents

    def write_corpus(self, file_path: Path, corpus: str) -> None:
        """Append the input string list to a file."""
        try:
            with file_path.open('a', encoding='utf-8') as f_corpus:
                f_corpus.write(corpus + "\n")
        except FileNotFoundError:
            print(f"File not found at: {file_path}")
            return []