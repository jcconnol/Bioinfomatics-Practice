#highest GC content
GC = 0
total = 0;
title = ""
GC_content = float(0)
highest_GC = float(0)
highest_title = ""

with open('problem4.txt', 'r') as f:
        while True:
                line = f.readline()
                if line == '':
                        break
                if line[:1] == ">":
                        title = line[1:]
                        line = f.readline()
                        while line[:1] != '>' or line != '':
                                for bp in line:
                                        total = total + 1
                                        if bp == "G" or bp == "C":
                                                GC = GC + 1
                                line = f.readline()
                                if line == '' or line[:1] != '>':
                                        break

                        GC_content = float(GC) / float(total)
                        if highest_GC < GC_content:
                                highest_GC = GC_content
                                highest_title = title
                        total = 0
                        GC = 0
                        
print highest_title,
print (highest_GC * 100)

f.closed


