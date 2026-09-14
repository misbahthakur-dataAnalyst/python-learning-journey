# print how many lines are present in notes.txt
import os


try:    
    with open("notes.txt","r") as f:
        listOfLines= f.readlines()
        print("output of readlines function", listOfLines)
        print("number of lines in file", len(listOfLines))
except:
    print("that files does notexist")

    # renaming file

os.rename("report.txt","madeeha.txt")
os.remove("madeeha.txt")
