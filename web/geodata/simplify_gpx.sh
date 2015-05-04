#!/bin/bash
# http://www.gpsbabel.org/htmldoc-1.5.0/filter_simplify.html

gpsbabel -t -i gpx -f $1 -x simplify,count=250 -o gpx -F $2
