#! python 3
# a program to loop through each filename in the current working directory and
# change to Europe style date

import shutil,os.re

dateRegex= re.compile(r"""^(.*?)   #all text before the date
    ((0|1)?\d) #all the month from 1 to 12
    ((0|1|2|3)?\d) #all the day of the month
    ((19|20)\d\d) #year 19xx and 20xx
    """,re.VERBOSE)

for Foldername in os.listdir('.'):
    find=dateRegex.search(Foldername)
    #Not finished

#TODO:skip the file without date

#TODO:Search the date in the filename

#TODO:Form the Europe date

#TODO:Get the absolute file path to change name using move

#TODO:Rename the file


