from spider import spider
from merge import merge
from finalmerge import finalmerges
import os
from delrepetition import delrepetitions
from convert import convert
from rename import renames

allpath = os.getcwd()
database = os.path.join(allpath, "train")

retry = 1
while retry:
    try:
        retry = 0
        spider(allpath)

    except:
        retry = 1
        print("START AGAIN")

merge(allpath)
print("Merged.")
finalmerges(allpath, database)
print("First finalmerged.")
delrepetitions(allpath)
print("Deleted.")
convert(allpath)
print("Converted.")
finalmerges(allpath, database)
print("Last finalmerged.")
renames(allpath)
print("All completed.")
