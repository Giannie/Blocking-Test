from __future__ import print_function
import argparse
import json
import itertools


def main():
    """Checks all combinations of options as given in the input file and prints impossible ones"""
    # Parse arguments to get blocking file
    parser = argparse.ArgumentParser(description="Returns a list of impossible combinations")
    parser.add_argument("file", metavar="Blocking_File", type=str, nargs=1,
                        help="File containing blocking data")
    parser.add_argument("--n", type=int, default=4, help="Number of subjects studied")
    args = parser.parse_args()
    filename = args.file[0]
    n = args.n

    # Load in blocking dict
    with open(filename, "r") as f:
        block_dict = json.loads(f.read())
    # Separate fm as a special case
    without_fm = [str(key) for key in block_dict.keys() if key != "fm"]
    without_ma = [str(key) for key in block_dict.keys() if key not in ["fm", "ma"]]
    # Consider all b combinations of size 4, print those that fail
    combos = itertools.combinations(without_fm, n)
    for combo in combos:
        if not test_combo(combo, [], block_dict):
            print("Fails:", combo)
    # Handle the fm case separately as only 3 subjects
    if "fm" in block_dict.keys() and n >= 2:
        combos = itertools.combinations(without_ma, n - 2)
        for combo in combos:
            combo = ("fm", "fm",) + combo
            if not test_combo(combo, [], block_dict):
                print("Fails:", combo)

    
def test_combo(combo, candidate, block_dict):
    """Backtracking function to check if a combination works"""
    if len(candidate) == len(combo):
        return True
    for block in block_dict[combo[len(candidate)]]:
        blocks = []
        for b in block:
            blocks.append(b)
        if not list_overlap(block, candidate):
            if test_combo(combo, candidate + blocks, block_dict):
                return True
    else:
        return False
    

def list_overlap(l1, l2):
    """Checks if any element of l1 is contained in l2"""
    for item in l1:
        if item in l2:
            return True
    return False


if __name__ == "__main__":
    main()