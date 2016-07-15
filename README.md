# File Pymover
**Version**: 1.0
**Last modified**: 2016-07-15
**Author**: Alex Gascon (https://github.com/AlexGascon)

The objective of this script is automatically moving files or folders whose name
matches certain conditions specified by a regular expression.


## DETAILS: 
In this specific example, I wanted to move all the folders I downloaded using the
script "coursera-dl" (https://github.com/coursera-dl/coursera-dl) from the general
path in which I have all my coursera courses into another one in which I have all
the courses whose material isn't classified and organized yet. 

The folders downloaded by the script have a name that follows a structure 
'{alphanum_string}-{numbers}'. We will also move the associated .json files that
are also created, whose name starts exactly with the same pattern. 

The parameters we have to change in order to adapt its execution to our needs are
*src_path*, *dst_path* and *pattern*, and can be found right at the beginning of
pyfilemover.py
