import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Returns a list of impossible combinations")
    parser.add_argument("file", metavar="Blocking_File", type=str, nargs=1,
                        help="File containing blocking data")
    args = parser.parse_args()
    filename = args.file[0]
    with open(filename, "r") as f:
        json.loads(f.read())


if __name__ == "__main__":
    main()