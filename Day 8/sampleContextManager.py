
allfiles = list()
for i in range(10000):
    outfile = open('anyfile', 'w')
    outfile.write('This is line 1\n')
    allfiles.append(outfile)
    outfile.close()

for i in range(10000):
    with open('anyfile', 'w') as outfile:
       outfile.write('This is line 1\n')
       allfiles.append(outfile)

