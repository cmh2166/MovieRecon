"""Harvest movie data from Google Spreadsheet, convert to dict/json."""
from argparse import ArgumentParser
import yaml


class RepoInvestigatorException(Exception):
    """Base exception for this script."""

    def __init__(self, value):
        """Base exception for this script."""
        self.value = value

    def __str__(self):
        """Base exception for this script."""
        return "%s" % (self.value,)


def main():
    """Main method for calling harvest with parameters."""
    parser = ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument("-i", "--input", dest="input",
                        help="URL for Google Sheet file.")
    parser.add_argument("-o", "--output", dest="output",
                        default="data/output.json",
                        help="Filename & directory for JSON output(s).")
    parser.add_argument("-u", "--username", dest="username",
                        help="Google Drive Authentication Username.")
    parser.add_argument("-p", "--password", dest="password",
                        help="Google Drive Authentication Password.")
    parser.add_argument("-c", "--config", dest="config",
                        help="Config file (YAML) for running this harvest.")
    args = parser.parse_args()

    if not args.input and not args.config:
        parser.print_help()
        parser.exit()

    if args.config:
        with open(args.config, 'r') as yamlfile:
            cfg = yaml.load(yamlfile)
            inputURL = cfg['googleAuth']['input']
            output = cfg['googleAuth']['output']
            username = cfg['googleAuth']['user']
            password = cfg['googleAuth']['password']
    else:
        inputURL = args.input
        output = args.output
        username = args.username
        password = args.password


if __name__ == '__main__':
    main()