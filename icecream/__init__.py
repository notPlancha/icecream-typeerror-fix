# -*- coding: utf-8 -*-

#
# IceCream - Never use print() to debug again
#
# Ansgar Grunseid
# grunseid.com
# grunseid@gmail.com
#
# License: MIT
#
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from os.path import dirname, join as pjoin

from .icecream import *  # noqa
from .builtins import install, uninstall

# Import all variables in __version__.py without explicit imports.
from . import __version__
globals().update(dict((k, v) for k, v in __version__.__dict__.items()))
