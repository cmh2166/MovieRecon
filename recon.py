"""Match movie data from Google-sourced JSON to various datasets."""
from argparse import ArgumentParser
import json
import pprint


class RepoInvestigatorException(Exception):
    """Base exception for this script."""

    def __init__(self, value):
        """Base exception for this script."""
        self.value = value

    def __str__(self):
        """Base exception for this script."""
        return "%s" % (self.value,)


def main():
    """Main method for performing recon with parameters."""
    parser = ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument("-i", "--input", dest="input",
                        default="data/output.json",
                        help="Original Google-sourced JSON data file.")
    parser.add_argument("-o", "--output", dest="output",
                        default="data/matched_output.json",
                        help="Matched JSON output data file.")
    parser.add_argument("-f", "--field", dest="field",
                        help="Field for easy review of metadata.")
    args = parser.parse_args()

    """Pull in Google-sourced JSON data."""
    with open(args.input, 'r') as fout:
        data = json.load(fout)
    keys = set()
    for n in data:
        for key in data[n].keys():
            keys.add(key)
    keys = list(keys)
    for key in sorted(keys):
        print(key)
        print("-----------------------------\n")
        values = set()
        for n in data:
            value = data[n][key]
            values.add(value)
        values = list(values)
        for value in sorted(values):
            print(value)
        print("========================================")


if __name__ == '__main__':
    main()