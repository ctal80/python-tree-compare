#!/usr/bin/env python3
import json


def t_read(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except (TypeError, OverflowError, ValueError) as exc:
                raise BadJSONError("Cannot decode object from JSON.\n%s" %
                                   str(exc))



def t_write(content, file, openmode='w'):
    try:
        with open(file, openmode) as f:
            f.write(content)
    except:
        print('Unexpected error writing to file %s' % file)
