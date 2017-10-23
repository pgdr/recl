# Rethink ecl

Thoughts of an improved ecl experience.

This is a working example of recl.

```python
#!/usr/bin/env python

from sys import argv
from recl import load_case

def main(case_path):
    case = load_case(case_path)
    grid = case.grid
    reg = grid.region()
    smry = case.summary
    init = case.init
    trx = init['TRANX']
    vol = sum([c.volume for c in grid if c.active])

if __name__ == '__main__':
    if len(argv) != 2:
        exit('Usage: kw.py CASE')
    case_path = argv[1]
    main(case_path)
```
