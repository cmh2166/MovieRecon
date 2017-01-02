"""Match movie data from Google-sourced JSON to various datasets."""
from argparse import ArgumentParser
import json
from norm import *
import requests

entity_types = ["Agent", "Form", "Genre", "Language", "Place", "Topic", "Work"]
s_agent_fields = ["Art Director", "DP/Cinematographer", "Director",
                  "Distributor", "Editor", "Music", "Producer",
                  "Production Company", "Script", "Stock brand"]
c_agent_fields = ["Copyright Owner", "Currently stored in", "Donated By:",
                  "Inspector's Name", "Labs used by filmmaker",
                  "Principal Cast", "Projectionist's Name"]
s_delimiters = ["|", ",", ";"]


class RepoInvestigatorException(Exception):
    """Base exception for this script."""

    def __init__(self, value):
        """Base exception for this script."""
        self.value = value

    def __str__(self):
        """Base exception for this script."""
        return "%s" % (self.value,)


def main():
    """Main method for performing recon on a field or entity type."""
    parser = ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument("-i", "--input", dest="input",
                        default="data/output.json",
                        help="Original Google-sourced JSON data file.")
    parser.add_argument("-o", "--output", dest="output",
                        default="data/matched_output.json",
                        help="Matched JSON output data file.")
    parser.add_argument("-f", "--field", dest="field",
                        help="Field for reconciliation.")
    parser.add_argument("-e", "--entity", dest="entity",
                        help="Entity type for reconciliation. See README.md")
    args = parser.parse_args()
    if not args.field and not args.entity:
        parser.print_help()
        parser.exit()

    """Pull in Google-sourced JSON data."""
    with open(args.input, 'r') as fout:
        data = json.load(fout)
    labels = []

    """Match against field or entity type field set."""
    for record in data:
        if args.field:
            if data[record][args.field]:
                val = data[record][args.field]
                if any(delim in val for delim in s_delimiters):
                    labels = field_split(val)
                else:
                    labels = [val.strip()]
        elif args.entity == "Agent":
            for field in s_agent_fields:
                if data[record][field]:
                    val = data[record][field]
                    if any(delim in val for delim in s_delimiters):
                        labels = field_split(val)
                    else:
                        labels = [val.strip()]
        pre_queries = {}
        for label in labels:
            key = "q" + str(labels.index(label))
            queries[key] = {}
            queries[key]["query"] = label
            queries[key]["type"] = "Names"
        queries = {}
        queries["queries"] = json.dumps(pre_queries)
        resp = requests.post("http://localhost:5000/", data=queries).json()
        print(resp["q0"])


if __name__ == '__main__':
    main()