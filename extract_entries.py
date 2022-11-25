# 161101014, Yasar Can Kakdas, Bil 334
# !/usr/bin/env python
import os
import re
import sys

if not len(sys.argv) > 1:
    print("Could not find a text file that contains entries")
    exit(0)

entries_file = sys.argv.pop()

if not os.path.exists(entries_file):
    print("Could not find the specified file named: " + entries_file)
    exit(0)

output_file = open(entries_file[:-4] + '_output.txt', 'w')

date_pattern = '^((19\d\d)|(20\d\d))-(0[1-9]|10|11|12)-(0[1-9]|1\d|2\d|30)'
username_pattern = '[_.]([A-Z]|[a-z]){3}\d{1,}[/]{0,1}'
ipv4_pattern = '(?!10\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

match_pattern = date_pattern + ' ' + username_pattern + ' ' + ipv4_pattern

# ((19\d\d)|(20\d\d)) : for 19xx and 20xx
# (0[1-9]|10|11|12) : for month between 01-12
# (0[1-9]|1\d|2\d|30) : for day between 01-30
# [_.] : user name starts with _ or .
# ([A-Z]|[a-z]){3} : at least 3 letter
# \d{1,} : at least one digit
# [/]{0,1} : optional
# (?!10\.) : ensures that ip address does not start with 10
# (([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.) : one length ip address from 0-9 or 2 length ip address between
# 10-99 or 3 length ip address between 100-255
# {3} : for xxx.xxx.xxx.
# last one should come without '.'

for line in open(entries_file):
    line = line.replace("\n", "")
    result = re.findall(match_pattern, line)
    if len(result) != 0:
        lastResult = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', line)
        output_file.write(lastResult + "\n")
output_file.close()
