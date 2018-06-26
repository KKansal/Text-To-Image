# File created

fp = open("files.txt", 'r')
fout = open("nouns_synid.txt", 'w')
count = 0
while count < 55:
	id = fp.readline().strip('\n')
	# print(id)
	fcsv = open(id + '.csv', 'r')
	line = fcsv.readline()
	s = set()
	count1 = 0
	while True:
		line = fcsv.readline()
		try:
			lemmas = line.split(',')
			lemmas = lemmas[2].split(';')
			for i in lemmas:
				s.add(i)
			count1 += 1
		except:
			print(count1, "lines read in file", count+1)
			break
	# print(s)
	fout.write(id)
	fout.write(" ")
	for i in s:
		fout.write(i)
		fout.write(",")
	fout.write('\n\n')
	count += 1

fp.close()
fout.close()