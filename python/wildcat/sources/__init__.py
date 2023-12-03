"""
Support for importing all sources at once, cf. http://stackoverflow.com/a/1057534/89391
"""

import glob
import os

modules = glob.glob("%s/*.py" % (os.path.dirname(__file__)))
__all__ = [os.path.basename(f)[:-3] for f in modules]
