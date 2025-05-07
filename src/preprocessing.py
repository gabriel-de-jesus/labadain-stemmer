#!/usr/bin/env python3
#
# src.preprocessing.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# 09-05-2024

class TextPreprocessing:
    """
    Class to preprocess input document, including:
    1. Lowercase the input text.
    2. Normalize aposthropes.
    """

    def __init__(self, text: str):
        self.text = text

    def lowercase_text(self) -> str:
        """Lowercase the input text."""
        return self.text.lower()

    def normalize_apostrophes(self) -> str:
        """Normalize apostrophe to a consistent character."""
        return self.text.replace("'", "’")

    def preprocess_text(self) -> str:
        """Preprocess the input text."""
        self.text = self.lowercase_text()
        preprocessed_text = self.normalize_apostrophes()
        return preprocessed_text