from calendar import c
from pickle import NONE
import MyUtils
from MainMgmt import MainMgmt
from pysql import pySQL

Mgmt = MainMgmt()

while True:
    ichoice = Mgmt._MainMenu()
    if not Mgmt._MyChoice(ichoice):
        break