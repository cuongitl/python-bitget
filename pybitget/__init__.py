"""An unofficial Python wrapper for the bitget exchange API v1

... moduleauthor: Cuongitl

"""

__version__ = '1.0.3'

from loguru import logger
from pybitget.client import Client
from pybitget import utils
from pybitget import exceptions
from pybitget.enums import *
