#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()  # remove leading and trailing whitespace
    columns = line.split(',')  # split line into parts by ','

    # check if every time we take a line from the file with the correct amount of columns
    if len(columns) == 15:
        try:
            # if it is NOT the first line
            if columns[0] != "ip":

                file = columns[6]
                accession = columns[5]

                # if extension (file) has no name only a suffix like ".txt" take accession as file name
                if file.startswith("."):
                    file = accession + file

                key = ','.join([columns[0], file])  # key=(ip,file name)
                value = columns[1]  # value=(date)
                print("%s\t%s" % (key, value))
        except ValueError:
            pass