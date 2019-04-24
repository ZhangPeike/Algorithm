#!/usr/bin/python2
import re
import os
import sys


# check an email name is valid or not
def IsValidEmail(str):
    # @
    # name [a-zA-Z0-9_]+
    # domain .
    pattern_ok = r'^[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+){0,4}@[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+){0,4}$'
    if re.match(pattern_ok, str):
        return True
    else:
        return False


if len(sys.argv) == 1:
    assert IsValidEmail('someone@gmail.com')
    assert IsValidEmail('bill.gates@microsoft.com')
    assert not IsValidEmail('bob#example.com')
    assert not IsValidEmail('mr-bob@example.com')