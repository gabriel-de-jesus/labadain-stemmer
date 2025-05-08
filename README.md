# Labadain Stemmer

## Description
Labadain Stemmer is a stemming algorithm specifically designed for Tetun. It focuses on stripping Portuguese-derived suffixes and commonly used affixes in Tetun (as listed in *config/tetun_affixes.py*), excluding circumfixes and reduplication. The Portuguese-derived suffixes are adapted from those used in the [Portuguese stemmer in Snowball](https://snowballstem.org/algorithms/portuguese/stemmer.html) and have been modified in accordance with loanword transformation rules established by the **Instituto Nacional de Linguística (INL)**. 

The Labadain Stemmer includes three variants:

- [ ] **Light:** Removes suffixes from Portuguese-derived words used in Tetun.

- [ ] **Moderate:** Extends the functionality of the *Light* variant by also removing suffixes from native Tetun words.

- [ ] **Heavy:** Builds on the functionality of the *Moderate* stemmer by additionally removing native Tetun prefixes.


## Dependencies

Install the dependencies specified in the `requirements` file.

```
pip install -r requirements.txt
```

## Usage

The Labadain Stemmer script can be run from the command line and supports both file-based and direct text input. You must specify either an input file or a text string, and optionally choose an output method and stemming mode.

### Basic syntax
```
python3 labadain_stemmer.py [-if INPUT_FILE | -it INPUT_TEXT] [-of OUTPUT_FILE | -ot] [-m MODE]
```

*Arguments:*

- [ ] *-if*: Path to an input text file.
- [ ] *-it*: A direct text string to stem (default).
- [ ] *-of*: Path to save the output.
- [ ] *-ot*: Print the stemmed result to the console (default).
- [ ] *-m*: Choose the stemming mode - light(default), moderate, heavy.

### Examples

- [ ] Stem a direct text string using *light* stemmer and print the result to console:

```
python3 labadain_stemmer.py -it "Komemorasaun loron independénsia Timor-Leste"
```

- [ ] Stem from a file using *moderate* stemmer and save output to another file:

```
python3 labadain_stemmer.py -if input.txt -of result.txt -m moderate
```


## Citation
If you use this repository or any of its contents for your research or academic work, please cite it as follows:

```
@misc{dejesus-nunes-2025,
      title={Establishing a Foundation for Tetun Text Ad-Hoc Retrieval: Stemming, Indexing, Retrieval, and Ranking}, 
      author={Gabriel de Jesus and S{\'e}rgio Nunes},
      year={2025},
      eprint={2412.11758},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2412.11758}
}
```