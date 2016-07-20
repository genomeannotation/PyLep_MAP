#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import os
import argparse
from src.controller import Controller

def main():
    parser = argparse.ArgumentParser(
    epilog="""
    PyLep_MAP: Python Lep-MAP pipeline\n
    Latest version at:\n
    https://github.com/genomeannotation/PyLep_MAP
    """,
    formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-p', '--plink_ped', help='path to .plink.ped file')
    parser.add_argument('-m', '--plink_map', help='path to .plink.map file')
    parser.add_argument('-v', '--vcf', help='path to .vcf file')
    parser.add_argument('-f', '--family', help='path to families.txt file', required=True)
    parser.add_argument('-r', '--rQTL', help='set this flag to run rQTL analysis', action='store_true')
    parser.add_argument('-ss', '--super_scaffold', help='set this flag to run Super-scaffold assembly analysis', action='store_true')
    args = parser.parse_args()
    controller = Controller()
    controller.execute(args)


if __name__ == '__main__':
    main()
