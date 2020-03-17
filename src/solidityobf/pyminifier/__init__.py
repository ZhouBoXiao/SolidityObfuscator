# -*- coding: UTF-8 -*-
# Meta
__version__ = '2.2'
__version_info__ = (2, 2)
__license__ = "GPLv3" # See LICENSE.txt
__author__ = 'Dan McDougall <daniel.mcdougall@liftoffsoftware.com>'

__doc__ = """\
**Python Minifier:**  Reduces the size of (minifies) Python code for use on
embedded platforms.

"""

# Import built-in modules
import os, sys, re, io
from optparse import OptionParser
from collections import Iterable

# Import our own modules
import minification
import token_utils
import obfuscate
import compression

py3 = False
lzma = False
bhasCCommentBegin = False

if not isinstance(sys.version_info, tuple):
    if sys.version_info.major == 3:
        py3 = True
        try:
            import lzma
        except ImportError:
            pass

# Regexes
multiline_indicator = re.compile('\\\\(\s*#.*)?\n')

# The test.+() functions below are for testing pyminifier...
def test_decorator(f):
    """Decorator that does nothing"""
    return f

def test_reduce_operators():
    """Test the case where an operator such as an open paren starts a line"""
    (a, b) = 1, 2 # The indentation level should be preserved
    pass

def test_empty_functions():
    """
    This is a test function.
    This should be replaced with 'def test_empty_functions(): pass'
    """

class test_class(object):
    "Testing indented decorators"

    @test_decorator
    def test_function(self):
        pass

def test_function():
    """
    This function encapsulates the edge cases to prevent them from invading the
    global namespace.
    """
    # This tests method obfuscation:
    method_obfuscate = test_class()
    method_obfuscate.test_function()
    foo = ("The # character in this string should " # This comment
           "not result in a syntax error") # ...and this one should go away
    test_multi_line_list = [
        'item1',
        'item2',
        'item3'
    ]
    test_multi_line_dict = {
        'item1': 1,
        'item2': 2,
        'item3': 3
    }
    this_line_has_leading_indentation    = '''<--That extraneous space should be
                                              removed''' # But not these spaces

def is_iterable(obj):
    """
    Returns `True` if *obj* is iterable but *not* if *obj* is a string, bytes,
    or a bytearray.
    """
    if isinstance(obj, (str, bytes, bytearray)):
        return False
    return isinstance(obj, Iterable)

def HandleCPlusPlusComment(lines, i):
    index = lines[i].find("//")
    if index != -1:
        lines[i] = lines[i][0:index]
        lines[i] += "\r\n"


def HandleCComment(lines, i):
    global bhasCCommentBegin
    while True:
        if not bhasCCommentBegin:
            index = lines[i].find("/*")
            if index != -1:
                bhasCCommentBegin = True
                index2 = lines[i].find("*/", index + 2)
                if index2 != -1:
                    lines[i] = lines[i][0:index] + lines[i][index2 + 2:]
                    bhasCCommentBegin = False  # continue look for comment
                else:
                    lines[i] = lines[i][0:index]  # only find "begin comment
                    lines[i] += "\r\n"
                    return -2
            else:
                return 0  # not find
        else:
            index2 = lines[i].find("*/")
            if index2 != -1:
                bhasCCommentBegin = False
                lines[i] = lines[i][index2 + 2:]  # continue look for comment
            else:
                return -1  # should delete this


def remove_comment(lines):
    global bhasCCommentBegin

    length = len(lines)
    i = 0
    while i < length:
        ret = HandleCComment(lines, i)
        if ret == -1:
            if bhasCCommentBegin == False:
                print ("There must be some wrong")
            del lines[i]
            i -= 1
            length -= 1
        elif ret == 0:
            HandleCPlusPlusComment(lines, i)
        else:
            pass
        i += 1
    return lines


def pyminify(options, _file):

    module = os.path.split(_file)[1]
    module = ".".join(module.split('.')[:-1])
    filesize = os.path.getsize(_file)
    source = open(_file, 'rb').read()
    tokens = token_utils.listified_tokenizer(source)

     # Perform obfuscation if any of the related options were set
    if options['obfuscate']:
        identifier_length = int(options['replacement_length'])
        name_generator = obfuscate.obfuscation_machine(identifier_length=identifier_length)
        obfuscate.obfuscate(module, tokens, options)

    result = token_utils.untokenize(tokens).strip()
    #result = filter(lambda x: x != '\r' and x != '\n', ' '.join(result.split()))
    print result
    # if options['outfile'] is not None:
    #     with open(options['outfile'], 'w') as f:
    #         f.write(result)
    #         f.close()
