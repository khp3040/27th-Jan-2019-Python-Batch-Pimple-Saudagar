
outfile = open('file.txt', 'w')
outfile.write('This is line 1\n')
outfile.write('This is line 2\n')
outfile.writelines(['This is line 3\n', 'This is line 4\n'])
outfile.close() # Always to write --

