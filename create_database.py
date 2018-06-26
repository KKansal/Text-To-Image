# file created
# import subprocess
# output = subprocess.check_output('ls')
# output = str(output)
# output = output.split('\\n')
# print(output)

# fp = open("files.txt", 'r')

# line = fp.readline()
# while(line != 'EOF'):
# 	if '.csv' not in line:
# 		print(line)
# 	line = fp.readline()

# fp.close()

import nltk
from nltk.corpus import wordnet

fp = open("files_without_0.txt", 'r')
fout = open("synset_nouns.txt", 'w')

count = 0
while count < 56:

	synset_id = fp.readline().strip('\n')
	synset_id = int(synset_id)
	# print(synset_id, type(synset_id))
	noun = wordnet.synset_from_pos_and_offset('n',synset_id)
	noun = str(noun)
	noun = noun[8:]
	noun = noun[:-7]
	fout.write(str(synset_id))
	fout.write(' ')
	fout.write(noun)
	count += 1
	fout.write('\n')

fout.close()
fp.close()