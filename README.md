# Blocking-Test

## Requirements:

Python 2.7 or greater (including any version of python 3).

### OR

Python 2.6 with argparse installed. (untested but should work)

## Usage:

To get a list of all combinations of three subjects that do not work:

python3 blocking.py example_file.json --n 3

## Blocking file:

The blocking file should be in json format, with keys representing subject codes and each key referencing a list of blocks available for that subject.

Each block should be in the format of a string. Subjects that are in two blocks at once can be referenced with a string of length 2.

See example_file.json for an example.