from spider import spiders
from finalmerge import finalmerges
import os
from delrepetition import delrepetitions
from convert import converts
from rename import renames

allpath = os.getcwd()
database = os.path.join(allpath, "train")

retry = 1
while retry:
    try:
        retry = 0
        spiders(allpath)

    except:
        retry = 1
        print("START AGAIN")


print("Download completed.")
finalmerges(allpath, database)
print("First merged.")
delrepetitions(allpath)
print("Deleted.")
converts(allpath)
print("Converted.")
finalmerges(allpath, database)
print("Last merged.")
renames(allpath)
print("All completed.")
