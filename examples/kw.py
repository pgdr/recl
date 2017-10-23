#!/usr/bin/env python

from __future__ import print_function

from sys import argv

from recl import load_case

def main(case_path):
    case = load_case(case_path)
    grid = case.grid
    reg = grid.region()
    smry = case.summary
    init = case.init
    trx = init['TRANX']
    print(trx)


if __name__ == '__main__':
    if len(argv) != 2:
        exit('Usage: kw.py CASE')
    case_path = argv[1]
    main(case_path)
