#A C T G output
f = open('rosalind_rna.txt', 'r')
for line in f:
	holder = ""
	for bp in line:
		if (bp == "A"):
			holder = holder + 'A'
		if (bp == "T"):
			holder = holder + 'U'
		if (bp == "G"):
			holder = holder + 'G'
		if (bp == "C"):
			holder = holder + 'C'
	print holder

f.closed


