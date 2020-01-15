import json


def t_read(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except:
        print('Unexpected error while reading %s' % file)


def t_write(content, file, openmode='w'):
    try:
        with open(file, openmode) as f:
            f.write(content)
    except:
        print('Unexpected error writing to file %s' % file)
