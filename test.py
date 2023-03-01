import os, time, re, sys
from dotenv import load_dotenv
from helium import *



txt = '$23,617,451'


print(re.sub('[$,]', '', txt))