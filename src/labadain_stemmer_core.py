from typing import List, Tuple

#!/usr/bin/env python3
#
# src.tetun_stemmer_core.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# 09-05-2024

TETUN_VOWELS = "aeiouáéíóú"


class LabadainStemmerCore:
    """Stemmer Core Class for Portuguese Loanwords."""

    def __init__(self):
        pass

    def find_r1_r2_positions(self, word: str) -> Tuple[int]:
        """
        Define the start positions of R1 and R2.
        R1 and R2 definitions: http://snowball.tartarus.org/texts/r1r2.html
        """
        r1 = len(word)
        r2 = len(word)

        # Find R1
        for i in range(1, len(word)):
            if word[i] not in TETUN_VOWELS and word[i-1] in TETUN_VOWELS:
                r1 = i + 1
                break

        # Find R2
        for i in range(r1 + 1, len(word)):
            if word[i] not in TETUN_VOWELS and word[i-1] in TETUN_VOWELS:
                r2 = i + 1
                break

        return r1, r2

    def find_rv_position(self, word: str) -> int:
        """
        Define the RV position.
        RV definition: http://snowball.tartarus.org/algorithms/spanish/stemmer.html
        """
        second_char_consonant = word[1] not in TETUN_VOWELS
        first_two_vowels = all(char in TETUN_VOWELS for char in word[:2])

        if len(word) < 3:
            return len(word)

        # Case 1: Second letter is a consonant, find the region after the next following vowel.
        if second_char_consonant:
            for i in range(2, len(word)):
                if word[i] in TETUN_VOWELS:
                    return i + 1
            return len(word)

        # Case 2: First two letters are vowels, find the region after the next consonant
        elif first_two_vowels:
            for i in range(2, len(word)):
                if word[i] not in TETUN_VOWELS:
                    return i + 1
            return len(word)

        else:
            # Case 3: Consonant-Vowel case, RV is the region after the third letter
            # Case 4: RV is the end of the word if these positions cannot be found
            return 3 if len(word) > 3 else len(word)

    def simple_replace_suffixes(self, word: str, suffixes: List[str], term_to_replace_suffix: str) -> str:
        """When a word terminates with "suffixes in the list", replace it with "term defined" if in R2."""
        _, r2 = self.find_r1_r2_positions(word)
        for suffix in suffixes:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index >= r2:
                return word[:suffix_index] + term_to_replace_suffix

        return word

    def process_amente_suffix(self, word: str, suffix: str) -> str:
        """
        When a word terminates with "amente" suffix:
        1. Delete if in R1.
        2. If preceded by iv, delete if in R2 (and if further preceded by at, delete if in R2), otherwise.
        3. If preceded by os, ic or ad, delete if in R2.
        """
        r1, r2 = self.find_r1_r2_positions(word)
        # Check if the suffix is in R1
        if word.endswith(suffix):
            suffix_index = len(word) - len(suffix)
            if suffix_index >= r1:
                # Check for "iv" preceding "amente"
                preceeding_iv = "iv"
                iv_index = word.rfind(preceeding_iv, 0, suffix_index)
                if iv_index != -1 and iv_index + len(preceeding_iv) == suffix_index:
                    # If 'iv' is in R2
                    if iv_index >= r2:
                        # Check for "at" preceding "iv"
                        preceeding_at = "at"
                        at_index = word.rfind(preceeding_at, 0, iv_index)
                        if at_index != -1 and at_index + len(preceeding_at) == iv_index:
                            if at_index >= r2:
                                return word[:at_index]
                    # Remove only "iv + amente" suffix if "at" preceeding is not found
                    return word[:iv_index]
                else:
                    preceedings = ["oz", "ik", "ad"]
                    for preceeding in preceedings:
                        preceeding_index = word.rfind(preceeding, 0, suffix_index)
                        if preceeding_index != -1 and preceeding_index + len(preceeding) == suffix_index:
                            if preceeding_index >= r2:
                                return word[:preceeding_index]
                # Remove only the "amente" suffix if no preceeding is found
                return word[:suffix_index]

        return word

    def process_mente_suffix(self, word: str, suffix: str) -> str:
        """
        When a word terminates with "mente":
        1. Delete if in R2.
        2. if preceded by "ante", "avel" or "ível", delete if in R2.
        """
        _, r2 = self.find_r1_r2_positions(word)
        if word.endswith(suffix):
            suffix_index = len(word) - len(suffix)
            if suffix_index >= r2:
                # Check for "ante", "avel", "ivel" preceding "mente"
                preceedings = ["ante", "avel", "ivel"]
                for preceeding in preceedings:
                    preceeding_index = word.rfind(preceeding, 0, suffix_index)
                    if preceeding_index != -1 and preceeding_index + len(preceeding) == suffix_index:
                        if preceeding_index >= r2:
                            return word[:preceeding_index]
                # Remove only the suffix if no preceeding is found
                return word[:suffix_index]

        return word

    def process_idades_suffixes(self, word: str, suffixes: List[str]) -> str:
        """
        When a word terminates with "idade" or "idades":
        1. Delete if in R2.
        2. If preceded by "abil", "is" or "iv", delete if in R2.
        """
        _, r2 = self.find_r1_r2_positions(word)
        for suffix in suffixes:
            if word.endswith(suffix):
                suffix_index = len(word) - len(suffix)
                if suffix_index >= r2:
                    # If preceded by "abil", "is" or "iv", delete if in R2.
                    preceedings = ["abil", "is", "iv"]
                    for preceeding in preceedings:
                        preceeding_index = word.rfind(preceeding, 0, suffix_index)
                        if preceeding_index != -1 and preceeding_index + len(preceeding) == suffix_index:
                            if preceeding_index >= r2:
                                return word[:preceeding_index]
                    # Remove only the suffix if no preceeding is found
                    return word[:suffix_index]

        return word

    def process_ivos_suffixes(self, word: str, suffixes: List[str]) -> str:
        """
        When a word terminates with "ivu", "iva, "ivus or "ivas":
        1. Delete if in R2
        2. If preceded by "at", delete if in R2
        """
        _, r2 = self.find_r1_r2_positions(word)
        for suffix in suffixes:
            if word.endswith(suffix):
                suffix_index = len(word) - len(suffix)
                if suffix_index >= r2:
                    # If preceded by "at", delete if in R2
                    preceeding = "at"
                    preceeding_index = word.rfind(preceeding, 0, suffix_index)
                    if preceeding_index != -1 and preceeding_index >= r2:
                        return word[:preceeding_index]
                    # Remove only the suffix if preceeding "at" is not found
                    return word[:suffix_index]

        return word

    def residual_suffixes_removal(self, word: str, suffixes: List[str]) -> str:
        """Delete suffix "a", "e", "i", "u", or "us", if in RV."""
        rv = self.find_rv_position(word)
        for suffix in suffixes:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index >= rv:
                return word[:suffix_index]

        return word

    def standard_suffix_removal(self, word: str, suffixes: List[str]) -> str:
        """Remove a suffix from the given word."""
        _, r2 = self.find_r1_r2_positions(word)
        sorted_suffixes = sorted(suffixes, key=len, reverse=True)
        for suffix in sorted_suffixes:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index >= r2:
                return word[:suffix_index]

        return word

    def verb_suffix_removal(self, word: str, suffixes: List[str]) -> str:
        """Remove a suffix from the given word."""
        rv = self.find_rv_position(word)
        sorted_suffixes = sorted(suffixes, key=len, reverse=True)
        for suffix in sorted_suffixes:
            suffix_index = len(word) - len(suffix)
            if word.endswith(suffix) and suffix_index >= rv:
                return word[:suffix_index]

        return word

    def tetun_suffix_removal(self, word: str, suffixes: List[str]) -> str:
        """Remove a suffix from the given word if the remaining root length is greater than two."""
        sorted_suffixes = sorted(suffixes, key=len, reverse=True)
        for suffix in sorted_suffixes:
            if word.endswith(suffix):
                stemmed_word = word[:-len(suffix)]
                # Remove the prefix if the length of the remaining word > 2
                if len(stemmed_word) > 2:
                    return stemmed_word

        return word

    def tetun_prefix_removal(self, word: str, prefixes: List[str]) -> str:
        "Remove a prefix from the given word if the remaining root length is greater than two."
        sorted_prefixes = sorted(prefixes, key=len, reverse=True)
        for prefix in sorted_prefixes:
            if word.startswith(prefix):
                stemmed_word = word[len(prefix):]
                # Remove the prefix if the length of the remaining word > 2
                if len(stemmed_word) > 2:
                    return stemmed_word

        return word