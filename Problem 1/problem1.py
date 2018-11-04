#A C T G output
A = 0
T = 0
G = 0
C = 0
f = open('rosalind_dna.txt', 'r')
for line in f:
	for bp in line:
		if (bp == "A"):
			A+=1
		if (bp == "T"):
			T+=1
		if (bp == "G"):
			G+=1
		if (bp == "C"):
			C+=1

print str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T)
f.closed


