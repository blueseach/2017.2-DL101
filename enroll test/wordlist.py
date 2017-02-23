

# -*- coding: utf-8 -*-
import io
import collections
import json
from collections import Counter

fh = open("happiness_seg.txt",'r')

#用' , '代替文章中的换行符
content = fh.read().replace('\n',' ， ').decode('utf8')
seglist = content.split()

binaryword = []
for i in range(0, len(seglist)-1):
    if(len(seglist[i]) >= 2 and len(seglist[i+1]) >= 2):
        binaryword.append(seglist[i]+" "+seglist[i+1])

words = Counter(binaryword)
topten = words.most_common(10)

for word in topten:
    print  " %s,%d" %(word[0], word[1])
