#A C T G output
f = open('rosalind_revc.txt', 'r')
for line in f:
	holder = ""
	for bp in line:
		if (bp == "A"):
			holder = 'T' + holder
		if (bp == "T"):
			holder = 'A' + holder
		if (bp == "G"):
			holder = 'C' + holder
		if (bp == "C"):
			holder = 'G' + holder
	print holder

f.closed


