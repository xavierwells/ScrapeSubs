# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:20:15 2020

@author: xavier wells

To use this code, take standard subtitle format srt and insert it into the working directory of this code
The file must be named subs.txt (change from .srt --> .txt)
the code will output a file with timestamps of word or character found and how many at the first
timestamp of the subtitle

"""


import re
import csv

# This method is derived from https://stackoverflow.com/a/38852821
def split_on_empty_lines(s):
    return re.split(r"(?:\r?\n){2,}", s.strip())

#MAIN
    
#Read in file to list of lists
file = open("subs.txt")
fileString = file.read()
split = split_on_empty_lines(fileString)
print("\n\n".join(split))


stringToFind = input("input the character or word or string youd like to find\n")

#Find all subtitle lists (in the list of lists) that contain "stringToFind
i = []
for paragraph in split:
    if paragraph.count(stringToFind) > 0:
        i.append(paragraph)

# generate the proper format for output of [timestamp, amount found]
totalCount = 0
timestamp = 0
interarrival = []
for element in i:
    totalcount = element.count(stringToFind)
    timestamp = element.splitlines()[1]
    timestamp = timestamp[:8]
    interarrival.append([timestamp, totalcount])
print(interarrival)
print(len(interarrival))

#output to CSV
with open("output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(interarrival)

file.close()

#Finding the actual interarrival times and data analysis was done in excel