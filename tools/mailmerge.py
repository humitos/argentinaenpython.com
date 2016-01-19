# -*- coding: utf-8 -*-

# EXAMPLE
# python mailmerge.py \
#   -i ~/Descargas/piura.csv \
#   -o /tmp/mailmerge-confirmados-piura.csv \
#   --title --strip \
#   --email 3 --first-name 1 --last-name 2 \
#   --url "http://argentinaenpython.com.ar/django-girls-piura/" \
#   --date "Sábado 23 de Enero de 2016" \
#   --city Piura \
#   --place "UDEP - Universidad de Piura, Av. Ramón Mugica 131, Piura, Piura, Perú" \
#   --hour "8:30 (puntual) a 18:30 hs." \
#   --days 5 \
#   --filter-column 21 --filter-column-text "Esperando respuesta"

"""Create .csv file to use with Mail Merge's Thunderbird plugin

Usage:
  mailmerge.py [(-v | --verbose)] [[options]] --input=IFILE --output=OFILE
  mailmerge.py --help
  mailmerge.py --version

Options:
  -i, --input IFILE            Input .csv file
  -o, --output IFILE           Output .csv file

  -e, --email=COLUMN           Email column
  -f, --first-name=COLUMN      FirstName column
  -l, --last-name=COLUMN       LastName column

  -c, --city=TEXT              City of the event
  -d, --date=TEXT              Date of the event
  -h, --hour=TEXT              Hour of the event
  -p, --place=TEXT             Place of the event
  -u, --url=TEXT               Url of the event
  -s, --days=TEXT              Days before event to confirm

  --filter-column=COLUMN          Apply filter on this column number
  --filter-column-text=TEXT       Look for this TEXT in the filtered row

  --title                      Apply .title() to the value
  --strip                      Apply .strip() to the value

  --help                       Show this screen
  -v --verbose                 Show the log in the standard output
  --version                    Show version
"""

import os
import csv
import logging
from docopt import docopt  # fades
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('mailmerge')
DIRNAME = os.path.dirname(os.path.abspath(__file__))


def setup_logging(verbose):
    logfile = os.path.join(DIRNAME, 'mailmerge.log')
    handler = RotatingFileHandler(logfile, maxBytes=1e6, backupCount=10)
    logger.addHandler(handler)
    formatter = logging.Formatter("%(asctime)s  %(name)-10s  "
                                  "%(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)

    if verbose:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='MailMerge 0.1')

    setup_logging(arguments['--verbose'])

    fields = [
        'city',
        'date',
        'days',
        'email',
        'first_name',
        'hour',
        'last_name',
        'place',
        'url',
    ]
    output = []
    output.append(fields)
    with open(arguments['--input'], 'r') as finput:
        reader = csv.reader(finput)
        for row in reader:
            if arguments['--filter-column']:
                filter_row = arguments['--filter-column']
                filter_text = arguments['--filter-column-text']
                if row[int(filter_row)] != filter_text:
                    continue

            orow = []
            for f in fields:
                argument = '--{}'.format(f.replace('_', '-'))
                if f in ['first_name', 'last_name', 'email']:
                    value = row[int(arguments[argument])]
                    if arguments['--title'] and f != 'email':
                        value = value.title()
                    if arguments['--strip']:
                        value = value.strip()
                    if f == 'email':
                        value = value.lower()
                    orow.append(value)
                else:
                    orow.append(arguments[argument])
            output.append(orow)

    with open(arguments['--output'], 'w') as foutput:
        writer = csv.writer(foutput)
        writer.writerows(output)

    print('File written at: {}'.format(arguments['--output']))
