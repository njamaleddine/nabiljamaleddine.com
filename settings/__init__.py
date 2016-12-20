# -*- coding: utf-8 -*-
from __future__ import print_function

# Standard Library
import sys

# CNNMoneyStream Version
__version__ = '1.0.8'

if "test" in sys.argv:
    print("\033[1;91mNo django tests.\033[0m")
    print("Try: \033[1;33mpy.test\033[0m")
    sys.exit(0)
