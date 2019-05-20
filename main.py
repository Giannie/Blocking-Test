import argparse


def main():
    description = "Returns a list of impossible combinations"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file", metavar="Blocking_File",
                        type=str, nargs=1,
                        help="File containing blocking data")
    args = parser.parse_args()
    print(args.file)


if __name__ == "__main__":
    main()