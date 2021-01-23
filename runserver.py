#!/usr/bin/env python
# -----------------------------------------------------------------------
# runserver.py
# Author: Isabel Zaller
# -----------------------------------------------------------------------

from sys import argv, exit, stderr
import argparse
from runapp import app


# -----------------------------------------------------------------------
# Add argument flags to this program and return the parsed arguments
def get_args():
    # Documentation: https://docs.python.org/3/library/argparse.html#
    parser = argparse.ArgumentParser(
        description='Atlassian Frontend Interview',
        allow_abbrev=False)
    parser.add_argument('port', type=int, nargs=1,
                        help='the port at which the server should listen')
    args = parser.parse_args()
    return args


def main(argv):
    args = get_args()
    port = int(args.port[0])

    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == '__main__':
    main(argv)
