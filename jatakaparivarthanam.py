#
# File: findmatch.py  /* Save the below code into a file named findmatch.py *.
# Pre-requisites
# Python 3.10.5
# pip 22.1.2 from C:\Users\priya\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
# Install the following imported packages (if not installed) using pip, after you install the above
# There is a bug with Python 3.7.x which did not allow pip to install pandasgui, so had to install Python 3.10.5
# If runnining into problems with older Python:
# https://pip.pypa.io/en/stable/installation/
# You might have to install the following:
# pip install pypiwin32
# pip install pywin32
# from PyPi: pip install pandasgui  (https://pypi.org/project/pandasgui/)
# pip install git+https://github.com/adamerose/pandasgui.git (test data for pandasgui)
#
import sys, getopt
import os.path
import csv
import pandas as pd
from pandasgui import show

#
# Wanted to try PyQt5 for GUI but pandasgui was easier and directly worked with pandas DataFrame
# The following are therefore not required
#from PyQt5.QtWidgets import QApplication, QMainWindow
#sys.path.append('\\PythonVersion\\lib\\site-packages\\win32')
#sys.path.append('\\PythonVersion\\lib\\site-packages\\win32\\lib')

# 
# Globals
# gdf - global DataFrame to be used by pandasgui
# DataFrame manipulation:
# https://www.statology.org/pandas-select-rows-based-on-column-values/
#
gdf = None

#
# Usage function
#
def checkusage(argv):
    
    if len(argv) == 0:
        print("Usage: findmatch.py [-i <inputfile> | --ifile <inputfile>] | [-h | --help]")
        sys.exit(1)

#
# The main function which does the command line processing.
#
def main(argv):
   
    global inputfile
   
    checkusage(argv)
    
    try:
        opts, args = getopt.getopt(argv,'i:h',['help', 'ifile='])
    except getopt.GetoptError:
        checkusage(argv)
    for opt, arg in opts:
        
        if opt in ('-h', '--help'):
            checkusage(argv)
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        else:
            checkusage(argv)


    file_exists = os.path.exists(inputfile)
    if not file_exists:
        print ("Input file does not exist")
        sys.exit(2)
    
#
# Reading the input file to identify the key fields to
# create the pdf receipt file, to send as receipts to 
# the donors.
# Simply reads the datafile into the global DataFrame
#       
def readFile(f):
    global gdf
    gdf = pd.read_csv (f)
    

#
# Calling the main routine to process the cmd line arguments.
#
if __name__ == "__main__":
   main(sys.argv[1:])

#
# The input file is being read for processing into a pdf receipt
# file for each donor in the input file.
#
readFile(inputfile)

'''
#
# Useful references:
# https://towardsdatascience.com/pandasgui-analyzing-pandas-dataframes-with-a-graphical-user-interface-36f5c1357b1d)
# https://www.analyticsvidhya.com/blog/2021/07/everything-you-need-to-know-about-pandasgui/#:~:text=PandasGUI%20is%20a%20Python%2Dbased,execute%20them%20under%20the%20hood.
# Filters can be created using the Filters dialog, some samples are:
# `Gothram* `=='Srivatsa'   /* Search for line items with Gothram Srivatsa */
# `Is your son / daughter aware of this registration? (initial screening form)*`=='No' /* search for awareness */
# Sophisticated regular expressions for search can be specified based on column names is possible:
# `Gothram* `.str.match('K.*')   /* Searches for all gothrams starting with K */
# Note: Multiple filters can be applied to arrive at the desired subset, and this subset can be exported as csv file
#
# Age calculation is pending based on the input file.
# For each row calculate age, this can be added to a new Age column in the data frame before invoking show(gdf):
# https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
# https://stackoverflow.com/questions/16327055/how-to-add-an-empty-column-to-a-dataframe
# https://www.stackvidhya.com/how-to-add-an-empty-column-to-pandas-dataframe/
#
'''
#
# Sample Addition of an empty Age column, this works!
# Now compute the age based on month and year of birth upto today and add for each row into Age cell
#
gdf['Age'] = ""
gui = show(gdf)
