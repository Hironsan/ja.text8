# -*- coding: utf-8 -*-
import fnmatch
import os

SAVE_FILE = 'tmp.txt'


def list_files(dirname):
    matches = []
    for root, dirnames, filenames in os.walk(dirname):
        for filename in fnmatch.filter(filenames, 'wiki*'):
            matches.append(os.path.join(root, filename))

    return matches


def read_files(filenames):
    for i, filename in enumerate(filenames):
        print('{}/{}'.format(i, len(filenames)))
        with open(filename) as f:
            yield f


def normalize(files):
    for f in files:
        for line in f:
            if line.startswith('<doc'):
                doc = []
                f.readline()  # skip title
                continue
            elif line.startswith('</doc>'):
                yield ''.join(doc)
            else:
                for c in line:
                    if c == '\n':
                        continue
                    elif c.isalpha():
                        doc.append(c.lower())
                    else:
                        doc.append(c)


def save(docs):
    with open(SAVE_FILE, 'w') as f:
        for doc in docs:
            f.write(doc + '\n')


if __name__ == '__main__':
    dirname = os.path.join(os.path.dirname(__file__), './extracted')
    filenames = list_files(dirname)
    files = read_files(filenames)
    texts = normalize(files)
    save(texts)
