# -*- coding: utf-8 -*

import re
import sys

script_file_folder = (re.match(".*\\\\", sys.argv[0])).group(0)

from modules.Parser import *

parser = Parser()
parser.main(sys.argv)
