# -*- coding: utf8 -*-

import os
import sys
import pandas as pd
import argparse
from views import jsonOut, teiOut

# Copyright 2020 James M. Tucker, PhD

# Translate Palaeographical Notebook into JSON datamodel

def parse_notebook(notebook):
    """
    Convert Palaeographical Notebook with Pandas. A notebook consists of three sheets: CHARs, SIGNs, and Frags.
    The CHARs and SIGNs sheets are indexed on the `roi_id`. This is the index used to keep the region of interest associated
    with its palaeographical description.
    """
    chars = pd.read_excel(notebook, sheet_name='CHARs', index_col='roi_id')
    signs = pd.read_excel(notebook, sheet_name='SIGNs', index_col='roi_id')
    frags = pd.read_excel(notebook, sheet_name='Frags')
    
    transcription = pd.merge(chars, signs, on='roi_id')
    
    return transcription


def convert_notebook(args):
    """
    Translate a palaeographical notebook into JSON format. This creates an interoperable format for machine reading purposes.
    :palaeo_notebook:
    :type: TEI or JSON
    """
    notebook = args.palaeo_notebook
    
    path, nb = os.path.split(notebook)
    name = os.path.splitext(nb)
    output = args.output.strip().lower()
    
    if output == 'tei' or output == 'json':
        df = parse_notebook(notebook)
        if output == 'json':
            jsonOut(df, name[0])
            # TODO prepare JSON out
        else:
            pass
            # TODO prepare TEI out
    else:
        print("Output type must be either JSON or TEI")
        quit

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
