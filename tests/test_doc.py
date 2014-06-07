#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test suite for the documentation of the pyunlocbox package.
"""

import doctest
import glob
import os
import unittest


files = []

# Test examples in docstrings.
base = os.path.join(os.path.dirname(__file__), os.path.pardir, 'pyunlocbox')
base = os.path.abspath(base)
files.extend(glob.glob(os.path.join(base, '*.py')))
files.extend(glob.glob(os.path.join(base, '*', '*.py')))

# Test examples in documentation.
base = os.path.join(os.path.dirname(__file__), os.path.pardir, 'docs')
base = os.path.abspath(base)
files.extend(glob.glob(os.path.join(base, '*.rst')))
files.extend(glob.glob(os.path.join(base, '*', '*.rst')))

assert files

suite = doctest.DocFileSuite(*files, module_relative=False, encoding='utf-8')


def run():
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run()
