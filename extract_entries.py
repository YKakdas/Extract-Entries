# 161101014, Yasar Can Kakdas, Bil 334
#!/usr/bin/env python

import sys
import re

entries_file=sys.argv.pop();
output_file=open(entries_file[:-4]+'_output.txt','w');

pattern='^((19\d\d)|(20\d\d))-(0[1-9]|10|11|12)-(0[1-9]|1\d|2\d|30) [_.]([A-Z]|[a-z]){3}\d{1,}[/]{0,1} ' \
        '(?!10\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$';
#((19\d\d)|(20\d\d)) : for 19xx and 20xx
#(0[1-9]|10|11|12) : for mounth between 01-12
#(0[1-9]|1\d|2\d|30) : for day between 01-30
#[_.] : user name starts with _ or .
#([A-Z]|[a-z]){3} : at least 3 letter
#\d{1,} : at least one digit
#[/]{0,1} : optionally
#(?!10\.) : ensures that ip address is not start with 10
#(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.) : one length ip address from 0-9 or 2 length ip address between
#10-99 or 3 length ip address between 100-255
#{3} : for xxx.xxx.xxx.
#last one should come without '.'
for line in open(entries_file) :
    result=re.findall(pattern,line);
    if(len(result)!=0) :
      lastResult=re.sub('(\d{4})-(\d{2})-(\d{2})',r'\3.\2.\1',line);
      output_file.write(lastResult);
output_file.close();