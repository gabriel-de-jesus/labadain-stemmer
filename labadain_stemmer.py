import argparse
from config.utils import Utils
from pathlib import Path
from typing import List
from tetuntokenizer.tokenizer import TetunSimpleTokenizer
from src.preprocessing import TextPreprocessing
from src.stemmer_pipeline import (
    LighStemmerPipeline,
    ModerateStemmerPipeline,
    HeavyStemmerPipeline
)

#!/usr/bin/env python3
#
# labadain_stemmer.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# 09-05-2024


class LabadainStemmer:
    """An implementation of the Labadain stemmer algorithm."""

    def __init__(self, text: str, mode: str = "light") -> None:
        self.text = text
        self.mode = mode
        self.tokenizer = TetunSimpleTokenizer()
        self.light_stemmer_pipe = LighStemmerPipeline()
        self.moderate_stemmer_pipe = ModerateStemmerPipeline()
        self.heavy_stemmer_pipe = HeavyStemmerPipeline()
        self.stemmed_words_list = []

    def tokenize_text(self) -> List[str]:
        """Remove punctuation, special characters, and tokenize into word and number tokens."""
        return self.tokenizer.tokenize(self.text)
    
    def light_stemmer(self) -> str:
        """Stem words to the root using light stemmer."""
        stemmed_words_list = []
        for word in self.tokenize_text():
            if len(word) > 3:
                stemmed_word = self.light_stemmer_pipe.light_stemmer(word.strip())
                stemmed_words_list.append(stemmed_word)
            else:
                stemmed_words_list.append(word)
        return " ".join(stemmed_words_list)

    def moderate_stemmer(self) -> str:
        """Stem words to the root using moderate stemmer."""
        for word in self.tokenize_text():
            if len(word) > 3:
                stemmed_word = self.moderate_stemmer_pipe.moderate_stemmer(word.strip())
                self.stemmed_words_list.append(stemmed_word)
            else:
                self.stemmed_words_list.append(word)
        return " ".join(self.stemmed_words_list)

    def heavy_stemmer(self) -> str:
        """Stem words to the root using heavy stemmer."""
        for word in self.tokenize_text():
            if len(word) > 3:
                stemmed_word = self.heavy_stemmer_pipe.heavy_stemmer(word.strip())
                self.stemmed_words_list.append(stemmed_word)
            else:
                self.stemmed_words_list.append(word)
        return " ".join(self.stemmed_words_list)


    def stem(self) -> str:
        if self.mode == "light":
            return self.light_stemmer()
        elif self.mode == "moderate":
            return self.moderate_stemmer()
        elif self.mode == "heavy":
            return self.heavy_stemmer()
        else:
            raise ValueError("Invalid mode! Choose 'light', 'moderate', or 'heavy'.")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Labadain Stemmer")

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("-if", "--input_file", type=str, help="Path to input text file")
    input_group.add_argument("-it", "--input_text",  type=str, help="Input string (default)")

    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-of", "--output_file", type=str, help="Path to save output text")
    output_group.add_argument(
        "-ot",
        "--output_text",
        action="store_true",
        help="Print output to console (default)")

    parser.add_argument(
        "-m",
        "--mode",
        choices=["light", "moderate", "heavy"],
        default="light",
        help="Choose stemming mode (default: light)"
    )
    args = parser.parse_args()

    # Load the input text
    utils = Utils()
    if args.input_file:
        text = utils.load_corpus(Path(args.input_file))
    else:
        text = args.input_text

    # Preprocessing
    text_preprocessor = TextPreprocessing(text)
    preprocessed_text = text_preprocessor.preprocess_text()

    # Stemming
    stemmer = LabadainStemmer(preprocessed_text, mode=args.mode)
    stemmed_text = stemmer.stem()

    # Output
    if args.output_file:
        utils.write_corpus(Path(args.output_file), stemmed_text)
    else:
        print(stemmed_text)