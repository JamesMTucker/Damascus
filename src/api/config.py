# -*- coding: utf8 -*-

# Copyright 2020 James M. Tucker, PhD
# configure functions for api and datamodel

from configparser import ConfigParser

def config_json(filename='static.ini', section='JSON'):
    """
    Get working directory for JSON datamodel
    :return: app directory for JSON
    """
    parser = ConfigParser()
    parser.read(filename)
    jsonDir = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            jsonDir[param[0]] = param[1]
    else:
        raise Exception('Section {} is not found in the {} file'.format(section, filename))
    return jsonDir

