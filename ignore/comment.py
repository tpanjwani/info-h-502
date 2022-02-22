# comment ipynb line

from nbconvert.filters import comment_lines
import nbformat

with open('test.ipynb') as f:
    nb = nbformat.read(f,as_version=4)

for c in nb.cells:
    if c['source'].startswith('%matplotlib widget'):
        c['source'] = f'# {c["source"]}'
        print(c)

with open('commented.ipynb','wt') as f:
    nb.write(f)


