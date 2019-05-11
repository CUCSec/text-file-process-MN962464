import os
import re
count=0
with open('log_files/201811123013.log',encoding='utf8')as f:
    for line in f:
        if(re.split('：|,',line)[3]=='201811123013'):
            count=count+1
print(count)