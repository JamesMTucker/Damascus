# -*- coding: utf8 -*-

# Copyright 2020 James M. Tucker, PhD
# All Rights Reserved

# Tucker, James M. “From Ink Traces to Ideology: Material, Text, and Composition of Qumran Community Rule Manuscripts.” Ph.D. Thesis, University of Toronto, 2021.

import os
import sys
import argparse
from notebook_convert import convert_notebook


def main(argv):
    """
    :palaeo_notebook: PATH to notebook
    :output: desired output type
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("palaeo_notebook", help="PATH to notebook", type=str)
    parser.add_argument("output", help="Convert to JSON or TEI", type=str)
    args = parser.parse_args()
    convert_notebook(args)


if __name__ == '__main__':
    main(sys.argv[1:])
