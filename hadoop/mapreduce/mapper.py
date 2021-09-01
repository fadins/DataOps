import sys

all_words = []
 
for i, line in enumerate(sys.stdin):
	if i == 0:
		continue
	one_line = (line.strip().split(','))    
	for k in one_line[0].split(' '):
        	all_words.append(k)
        for i in all_words:
            print('{},1\n'.format(i))