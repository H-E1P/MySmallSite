from sys import argv as _a
from MYSMALLSITE.gener import _read, _write, _if

def fixer(filename):
    '''
    fix file what ends with enter 2 without enter.
    '''
    assert _if(filename), FileNotFoundError(filename)
    src = _read(filename)
    if src[-1] == '\n': write(_filename, src[:-1])

def cli():
    l = len(_a)
    assert l < 3, ArgumentError("fixer's parameter must be one file path or non(to input)")
    a = _a[1] if l - 1 else input("file : ")
    fixer(a)