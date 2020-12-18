# -*- encoding: utf8 -*-

# Copyright 2020 James M. Tucker, PhD
# University of Toronto

class scribal_hand:
    """
    Translate scribal hand from an imaged fragment or artefact into a digital representation
    """
    def __init__(self):
        self

        
    def hebGlyphs(self):
        """
        Define unicode glyphs for Jewish Square Script
        """
        self.charGlyphs = {}

        charGlyphs = {
            1: {'unicode': "א", 'hex': "U+05D0", 'xhtml': '&#1488;', 'acc': 'a', 'tei': 'c'},
            2: {'unicode': "ב", 'hex': "U+05D1", 'xhtml': '&#1489;', 'acc': 'b', 'tei': 'c'},
            3: {'unicode': "ג", 'hex': "U+05D2", 'xhtml': '&#1490;', 'acc': 'g', 'tei': 'c'},
            4: {'unicode': "ד", 'hex': "U+05D3", 'xhtml': '&#1491;', 'acc': 'd', 'tei': 'c'},
            5: {'unicode': "ה", 'hex': "U+05D4", 'xhtml': '&#1492;', 'acc': 'h', 'tei': 'c'},
            6: {'unicode': "ו", 'hex': "U+05D5", 'xhtml': '&#1493;', 'acc': 'w', 'tei': 'c'},
            7: {'unicode': "ז", 'hex': "U+05D6", 'xhtml': '&#1494;', 'acc': 'z', 'tei': 'c'},
            8: {'unicode': "ח", 'hex': "U+05D7", 'xhtml': '&#1495;', 'acc': 'j', 'tei': 'c'},
            9: {'unicode': "ט", 'hex': "U+05D8", 'xhtml': '&#1496;', 'acc': 'f', 'tei': 'c'},
            10: {'unicode': "י", 'hex': "U+05D9", 'xhtml': '&#1497;', 'acc': 'y', 'tei': 'c'},
            11: {'unicode': "כ", 'hex': "U+05DB", 'xhtml': '&#1499;', 'acc': 'k', 'tei': 'c'},
            12: {'unicode': "ך", 'hex': "U+05DA", 'xhtml': '&#1498;', 'acc': 'K', 'tei': 'c'},
            13: {'unicode': "ל", 'hex': "U+05DC", 'xhtml': '&#1500;', 'acc': 'l', 'tei': 'c'},
            14: {'unicode': "מ", 'hex': "U+05DE", 'xhtml': '&#1502;', 'acc': 'm', 'tei': 'c'},
            15: {'unicode': "ם", 'hex': "U+05DD", 'xhtml': '&#1501;', 'acc': 'M', 'tei': 'c'},
            16: {'unicode': "נ", 'hex': "U+05E0", 'xhtml': '&#1504;', 'acc': 'n', 'tei': 'c'},
            17: {'unicode': "ן", 'hex': "U+05DF", 'xhtml': '&#1503;', 'acc': 'N', 'tei': 'c'},
            18: {'unicode': "ס", 'hex': "U+05E1", 'xhtml': '&#1505;', 'acc': 's', 'tei': 'c'},
            19: {'unicode': "ע", 'hex': "U+05E2", 'xhtml': '&#1506;', 'acc': 'o', 'tei': 'c'},
            20: {'unicode': "פ", 'hex': "U+05E4", 'xhtml': '&#1508;', 'acc': 'p', 'tei': 'c'},
            21: {'unicode': "ף", 'hex': "U+05E3", 'xhtml': '&#1507;', 'acc': 'P', 'tei': 'c'},
            22: {'unicode': "צ", 'hex': "U+05E6", 'xhtml': '&#1510;', 'acc': 'x', 'tei': 'c'},
            23: {'unicode': "ץ", 'hex': "U+05E5", 'xhtml': '&#1509;', 'acc': 'X', 'tei': 'c'},
            24: {'unicode': "ק", 'hex': "U+05E7", 'xhtml': '&#1511;', 'acc': 'q', 'tei': 'c'},
            25: {'unicode': "ר", 'hex': "U+05E8", 'xhtml': '&#1512;', 'acc': 'd', 'tei': 'c'},
            26: {'unicode': "ש", 'hex': "U+05E9", 'xhtml': '&#1513;', 'acc': 'C', 'tei': 'c'},
            27: {'unicode': "ת", 'hex': "U+05EA", 'xhtml': '&#1514;', 'acc': 't', 'tei': 'c'},
        }
        return charGlyphs

    def diacriticsGlyphs():
        """
        Define diacritic marks for transcription
        """
        diacriticGlyphs = {
            1: {'unicode': "◦", 'hex': "U+25E6", 'xhtml': '&#9702;', 'acc': '', 'tei': ''},
            2: {'unicode': "s", 'hex': "U+0073", 'xhtml': 's', 'acc': '', 'tei': ''},
            3: {'unicode': "m", 'hex': "U+006D", 'xhtml': 'm', 'acc': '', 'tei': ''},
            4: {'unicode': "v", 'hex': "U+0076", 'xhtml': 'v', 'acc': '', 'tei': ''},
            5: {'unicode': "v_a", 'hex': "", 'xhtml': '', 'acc': '', 'tei': ''},
            6: {'unicode': "v_u", 'hex': "", 'xhtml': '', 'acc': '', 'tei': ''},
            7: {'unicode': "v_i", 'hex': "", 'xhtml': '', 'acc': '', 'tei': ''},
            8: {'unicode': "d", 'hex': "", 'xhtml': '&#1491;', 'acc': 'd', 'tei': ''},
            9: {'unicode': "x", 'hex': "", 'xhtml': '&#1491;', 'acc': 'd', 'tei': ''},
            10: {'unicode': "_", 'hex': "U+0020", 'xhtml': ' ', 'acc': ' ', 'tei': ''}
        }
        return diacriticGlyphs

def cryptic_script():
    """
    """
    pass

def validation():
    """
    Create validation list of signs for palaeographical notebook
    """
    validate = []
    chars = hebGlyphs()
    diacritics = diacriticsGlyphs()

    for item in chars.items():
        validate.append(item[1]['unicode'])
    
    for item in diacritics.items():
        validate.append(item[1]['unicode'])
    
    return validate