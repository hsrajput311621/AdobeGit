import os

file1 = open('logmainline237fd.txt', 'r')
file2 = open('logmain6a7e6bc79_20221109.txt', 'r')

diff = ''

for line1, line2 in zip(file1, file2):
    if line1 != line2:
        diff += 'Line from file 1: ' + line1 + 'Line from file 2: ' + line2

file1.close()
file2.close()

if diff == '':
    print('Files are identical')
else:
    file3 = open('file3.txt', 'w')
    file3.write(diff)
    file3.close()
    print('Differences written to file3.txt')
