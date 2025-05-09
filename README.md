# Labadain Stemmer

## Description
Labadain Stemmer is a stemming algorithm specifically designed for Tetun. It focuses on stripping Portuguese-derived suffixes and Tetun commonly used affixes (as listed in *config/tetun_affixes.py*), excluding circumfixes and reduplication. The Portuguese-derived suffixes are adapted from those used in the [Portuguese stemmer in Snowball](https://snowballstem.org/algorithms/portuguese/stemmer.html) and have been modified in accordance with loanword transformation rules established by the **Instituto Nacional de Linguística (INL)**. 

The Labadain Stemmer includes three variants:

- [ ] **Light:** Removes suffixes from Portuguese-derived words used in Tetun.

- [ ] **Moderate:** Extends the functionality of the *light* variant by also removing suffixes from native Tetun words.

- [ ] **Heavy:** Builds on the functionality of the *moderate* variant by additionally removing native Tetun prefixes.


## Getting started

To get started with the Labadain Stemmer, first clone the repository from GitHub:

```
$ git clone https://github.com/gabriel-de-jesus/labadain-stemmer.git

```

Then navigate into the project directory:
```
cd labadain-stemmer
```

You may also want to set up a virtual environment and activate it:

```
python3 -m venv .labadain-stemmer
source .labadain-stemmer/bin/activate
```

Install the required dependencies in the `requirements.txt` file:

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
- [ ] *-it*: An input string to stem (default).
- [ ] *-of*: Path to save the output.
- [ ] *-ot*: Print the stemmed result to the console (default).
- [ ] *-m*: Choose the stemming mode - light (default), moderate, heavy.

### Examples

- [ ] Stem an input text using *light* stemmer and print the result to console:

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
      title={Establishing a Foundation for Tetun Ad-Hoc Text Retrieval: Stemming, Indexing, Retrieval, and Ranking}, 
      author={Gabriel de Jesus and S{\'e}rgio Nunes},
      year={2025},
      eprint={2412.11758},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2412.11758}
}
```