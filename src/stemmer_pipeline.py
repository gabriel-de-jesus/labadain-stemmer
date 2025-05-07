from src.labadain_stemmer_core import LabadainStemmerCore
from config import tetun_affixes as affix

#!/usr/bin/env python3
#
# src.stemmer_pipeline.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# 09-05-2024


class LighStemmerPipeline(LabadainStemmerCore):
    """Labadain Stemmer Pipeline."""

    def __init__(self) -> None:
        pass

    def light_stemmer(self, word: str) -> str:
        """Pipeline to execute the Labadain Stemmer algorithm."""
        # === Step 1 - Standard suffix removal ===
        if word.endswith(tuple(affix.general_suffixes)):
            return self.standard_suffix_removal(word, affix.general_suffixes)

        # "lojia" or "lojias" endings
        elif word.endswith(tuple(affix.lojias_suffixes)):
            return self.simple_replace_suffixes(word, affix.lojias_suffixes, "loj")

        # "usaun" or "usoens" endings
        elif word.endswith(tuple(affix.usoens_suffixes)):
            return self.simple_replace_suffixes(word, affix.usoens_suffixes, "u")

        # "énsia" or "énsias" endings
        elif word.endswith(tuple(affix.ensias_suffixes)):
            return self.simple_replace_suffixes(word, affix.ensias_suffixes, "ente")

        # "amente" ending
        elif word.endswith(affix.amente_suffix):
            return self.process_amente_suffix(word, affix.amente_suffix)

        # "mente" ending
        elif word.endswith(affix.mente_suffix):
            return self.process_mente_suffix(word, affix.mente_suffix)

        # "idade" or "idades" suffixes
        elif word.endswith(tuple(affix.idades_suffixes)):
            return self.process_idades_suffixes(word, affix.idades_suffixes)

        # "ivu", "iva", "ivus", or "ivas" suffixes
        elif word.endswith(tuple(affix.ivos_suffixes)):
            return self.process_ivos_suffixes(word, affix.ivos_suffixes)

        # === Step 2 - Verb suffixes removal ===
        elif word.endswith(tuple(affix.verb_based_suffixes)):
            return self.verb_suffix_removal(word, affix.verb_based_suffixes)

        # === Step 3 (step 4 in Snowball) - Residual suffix removal
        elif word.endswith(tuple(affix.residual_suffixes)):
            return self.residual_suffixes_removal(word, affix.residual_suffixes)

        # Return original word if it doesn't match the previous rules
        else:
            return word


class ModerateStemmerPipeline(LabadainStemmerCore):
    """Labadain Stemmer Pipeline."""

    def __init__(self) -> None:
        pass

    def moderate_stemmer(self, word: str) -> str:
        """Pipeline to execute the Labadain Stemmer algorithm."""
        # === Step 1 - Standard suffix removal ===
        if word.endswith(tuple(affix.general_suffixes)):
            return self.standard_suffix_removal(word, affix.general_suffixes)

        # "lojia" or "lojias" endings
        elif word.endswith(tuple(affix.lojias_suffixes)):
            return self.simple_replace_suffixes(word, affix.lojias_suffixes, "loj")

        # "usaun" or "usoens" endings
        elif word.endswith(tuple(affix.usoens_suffixes)):
            return self.simple_replace_suffixes(word, affix.usoens_suffixes, "u")

        # "énsia" or "énsias" endings
        elif word.endswith(tuple(affix.ensias_suffixes)):
            return self.simple_replace_suffixes(word, affix.ensias_suffixes, "ente")

        # "amente" ending
        elif word.endswith(affix.amente_suffix):
            return self.process_amente_suffix(word, affix.amente_suffix)

        # "mente" ending
        elif word.endswith(affix.mente_suffix):
            return self.process_mente_suffix(word, affix.mente_suffix)

        # "idade" or "idades" suffixes
        elif word.endswith(tuple(affix.idades_suffixes)):
            return self.process_idades_suffixes(word, affix.idades_suffixes)

        # "ivu", "iva", "ivus", or "ivas" suffixes
        elif word.endswith(tuple(affix.ivos_suffixes)):
            return self.process_ivos_suffixes(word, affix.ivos_suffixes)

        # === Step 2 - Verb suffixes removal ===
        elif word.endswith(tuple(affix.verb_based_suffixes)):
            return self.verb_suffix_removal(word, affix.verb_based_suffixes)

        # === Tetun native ===

        # Tetun suffixes removal
        elif word.endswith(tuple(affix.tetun_suffixes)):
            return self.tetun_suffix_removal(word, affix.tetun_suffixes)

        # === Step 3 (step 4 in Snowball) - Residual suffix removal
        elif word.endswith(tuple(affix.residual_suffixes)):
            return self.residual_suffixes_removal(word, affix.residual_suffixes)

        # Return original word if it doesn't match the previous rules
        else:
            return word


class HeavyStemmerPipeline(LabadainStemmerCore):
    """Labadain Stemmer Pipeline."""

    def __init__(self) -> None:
        pass

    def heavy_stemmer(self, word: str) -> str:
        """Pipeline to execute the Labadain Stemmer algorithm."""
        # === Step 1 - Standard suffix removal ===
        if word.endswith(tuple(affix.general_suffixes)):
            return self.standard_suffix_removal(word, affix.general_suffixes)

        # "lojia" or "lojias" endings
        elif word.endswith(tuple(affix.lojias_suffixes)):
            return self.simple_replace_suffixes(word, affix.lojias_suffixes, "loj")

        # "usaun" or "usoens" endings
        elif word.endswith(tuple(affix.usoens_suffixes)):
            return self.simple_replace_suffixes(word, affix.usoens_suffixes, "u")

        # "énsia" or "énsias" endings
        elif word.endswith(tuple(affix.ensias_suffixes)):
            return self.simple_replace_suffixes(word, affix.ensias_suffixes, "ente")

        # "amente" ending
        elif word.endswith(affix.amente_suffix):
            return self.process_amente_suffix(word, affix.amente_suffix)

        # "mente" ending
        elif word.endswith(affix.mente_suffix):
            return self.process_mente_suffix(word, affix.mente_suffix)

        # "idade" or "idades" suffixes
        elif word.endswith(tuple(affix.idades_suffixes)):
            return self.process_idades_suffixes(word, affix.idades_suffixes)

        # "ivu", "iva", "ivus", or "ivas" suffixes
        elif word.endswith(tuple(affix.ivos_suffixes)):
            return self.process_ivos_suffixes(word, affix.ivos_suffixes)

        # === Step 2 - Verb suffixes removal ===
        elif word.endswith(tuple(affix.verb_based_suffixes)):
            return self.verb_suffix_removal(word, affix.verb_based_suffixes)

        # Tetun suffixes removal
        elif word.endswith(tuple(affix.tetun_suffixes)):
            return self.tetun_suffix_removal(word, affix.tetun_suffixes)

        # Tetun prefixes removal
        elif word.startswith(tuple(affix.tetun_prefixes)):
            return self.tetun_prefix_removal(word, affix.tetun_prefixes)

        # === Step 3 (step 4 in Snowball) - Residual suffix removal
        elif word.endswith(tuple(affix.residual_suffixes)):
            return self.residual_suffixes_removal(word, affix.residual_suffixes)

        # Return original word if it doesn't match the previous rules
        else:
            return word