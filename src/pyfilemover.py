"""
File Pymover
Version: 1.0
Last modified: 2016-07-15
Author: Alex Gascon (https://github.com/AlexGascon)

The objective of this script is automatically moving files or folders whose name
matches certain conditions specified by a regular expression.


DETAILS: 
In this specific example, I wanted to move all the folders I downloaded using the
script "coursera-dl" (https://github.com/coursera-dl/coursera-dl) from the general
path in which I have all my coursera courses into another one in which I have all
the courses whose material isn't classified and organized yet. 

The folders downloaded by the script have a name that follows a structure 
'{alphanum_string}-{numbers}'. We will also move the associated .json files that
are also created, whose name starts exactly with the same pattern. 
"""

import os, shutil, re

# Source and destination path
src_path = "D:\Documentos\Coursera.org"
dst_path = "D:\Documentos\Coursera.org\NOT CLASSIFIED"
# Regex pattern that needs to be matched (in this case '{alphanum_str}-{numbers}')
pattern = "\w+-\d+"


# Getting files and folders in the source directory
origin_content = os.listdir(src_path)

# Files that match the regex pattern specified
# What we do here is use list comprehension in order to iterate over all the
# elements of origin_content and add to the array only those that match the regex
# (i.e. the matched string has one char or more)
to_move = [content for content in origin_content if len(re.findall(pattern, content)) > 0]

# Moving the files
for element in to_move:
	# Getting the complete name (path + name) of the element we're moving
	full_src_path = src_path + os.sep + element
	shutil.move(full_src_path, dst_path)





