from __future__ import print_function
import argparse
import json
import itertools


def main():
    """Main function to print failed combinations"""

    # Parse arguments to get blocking file
    description = "Returns a list of impossible combinations"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file", metavar="Blocking_File", type=str, nargs=1,
                        help="File containing blocking data")
    parser.add_argument("--n", type=int, default=4,
                        help="Number of subjects studied")
    args = parser.parse_args()
    filename = args.file[0]
    n = args.n

    # Load in blocking dict
    with open(filename, "r") as f:
        block_dict = json.loads(f.read())

    # Test every combo and print those that fail
    for failure in test_all_combos(block_dict, n):
        print(failure)


def test_all_combos(block_dict, n):
    """Finds all failing combos from a blocking dictionary"""
    # Separate fm as a special case
    without_fm = [str(key) for key in block_dict.keys() if key != "fm"]
    without_fm.sort()
    without_ma = [str(key) for key in block_dict.keys()
                  if key not in ["fm", "ma"]]
    without_ma.sort()

    # Consider all bad combinations of size 4, print those that fail
    failures = []
    combos = itertools.combinations(without_fm, n)
    for combo in combos:
        if not test_combo(combo, [], block_dict):
            failures.append(combo)

    # Handle the fm case separately as only 3 subjects
    if "fm" in block_dict.keys() and n >= 2:
        combos = itertools.combinations(without_ma, n - 2)
        for combo in combos:
            combo = ("fm", "fm",) + combo
            if not test_combo(combo, [], block_dict):
                failures.append(combo)
    return failures


def test_combo(combo, candidate, block_dict):
    """
    Backtracking function to check if a combination works

    combo is the subject combo
    candidate stores the potential blocking
    block_dict stores the blocking structure for each subject
    """

    # If candidate is same length as combo, a blocking has been found
    if len(candidate) == len(combo):
        return True

    # Iterate over all blocks in the next subject
    for block in block_dict[combo[len(candidate)]]:
        # Handle subjects in multiple blocks
        blocks = []
        for b in block:
            blocks.append(b)

        # Try a block for a subject
        if not list_overlap(block, candidate):
            if test_combo(combo, candidate + blocks, block_dict):
                return True

    # Return False if we run out of possible blocks
    else:
        return False


def list_overlap(l1, l2):
    """Checks if any element of l1 is contained in l2"""
    for item in l1:
        if item in l2:
            return True
    return False


def is_dependent_combo(combo, combos):
    """Checks if a combination is already caught in a smaller subject combo"""
    # Can't had a combo less than 3 fail
    if len(combo) <= 2:
        return False

    # Check all smaller combinations of combo and check if any are in combos
    for i in range(2, len(combo)):
        for sub in itertools.combinations(combo, i):
            if sub in combos:
                return True
    return False


if __name__ == "__main__":
    main()
