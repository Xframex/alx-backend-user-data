#!/usr/bin/env python3

import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(r'(?<!\S)(' + '|'.join(fields) + r')=[^;]*', lambda x: x.group(1) + '=' + redaction, message)
