# -*- encoding: utf8 -*-

# Copyright 2020 James M. Tucker, PhD.

import pandas as pd
from config import config_json
import json
import os

def jsonOut(df):
    """
    Translate pandas dataframe into json
    """
    output = config_json()
    
    #remove unnecessary columns
    df.drop(["editors_sigla_id", "he_mach", "kerning", "damaged", "damaged_vis", "line_status_int", "line_status_mid", "line_status_end", "iaa_related_to", "pam_related_to", "Area", "Mean", "Min", "Max", "Major", "Minor", "Angle", "Circ.", "AR", "Round", "Solidity"], axis=1, inplace=True)
    
    #prepare json output file
    data = df.to_json(orient="index")
    parsed = json.loads(data)
    with open(os.path.join(output['json'], 'TS-10KS-1r.json'), 'w') as f:
        json.dump(parsed, f, indent=4)


def teiOut(df):
    """
    Translate pandas dataframe into tei
    """
    pass