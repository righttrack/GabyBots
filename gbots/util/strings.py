__author__ = 'jeffmay'

def is_control_char(c):
    return ord(c) < 32 and c not in ('\t', '\n', '\r')

def clean_control_chars(string):
    return ''.join(c for c in string if not is_control_char(c))