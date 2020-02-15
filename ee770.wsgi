#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ee770/")

from ee770 import app2 as application
from ee770 import plot 
from ee770 import plot2
#from ee770 import forms
#from ee770 import assn2_module
#from ee770 import assn3_module
#from ee770 import proj_module
