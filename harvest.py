"""Harvest movie data from Google Spreadsheet, convert to dict/json."""
from argparse import ArgumentParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


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
    parser.add_argument("-c", "--config", dest="cfg",
                        help="Config file (JSON) for running Google Apps.")
    args = parser.parse_args()
    if not args.input or not args.cfg:
        parser.print_help()
        parser.exit()

    """Set up for accessing Google Sheet with document."""
    sheet = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(args.cfg, sheet)
    drive = gspread.authorize(creds)
    ssheet = drive.open_by_url(args.input)
    data = ssheet.sheet1.get_all_values()
    header = data[0]

    """Generating dictionary from Google Sheet data."""
    output_dict = {}
    for m in data[1:]:
        internal_dict = {}
        for n in range(len(m)):
            # Remove annoying Windows-based(Access?) encoding from orig data.
            value = m[n].strip("\ufffd")
            value = value.replace("\ufffd", " | ")
            value = value.replace("\u2026", "...").replace("\u201c", '"')
            value = value.replace("\u201d", '"').replace("\u2019", "'")
            internal_dict[header[n]] = value
        output_dict[data.index(m)] = internal_dict

    """Writing Dictionary to Json Output file."""
    with open(args.output, 'w') as fout:
        json.dump(output_dict, fout)


if __name__ == '__main__':
    main()