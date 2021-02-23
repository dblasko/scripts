readFile = input('Input file : ')
writeFile = input('Output file : ')

file_r = open(readFile, 'r')
header = file_r.readline().split(",")
lines_r = file_r.readlines()
file_r.close()

file_w = open(writeFile, 'w')
lines_w = []

counter = 0
print('Columns :')
for col in header:
    print("   {} - index {}".format(col.strip("\n"), counter))
    counter +=1
cols = input('Indexes of the columns to keep, between 0 and {}, separed by spaces : '.format(len(header)-1))
colsToKeep = []
for col in cols.split(' '):
    col_val = int(col)
    if col_val >= 0 and col_val < len(header):
        colsToKeep.append(col_val)

for line in lines_r:
    s = line.split(",")
    for col in colsToKeep:
        lines_w.append(s[col].strip('\n'))
        lines_w.append(' ')
    if len(colsToKeep) > 0:
        lines_w.append('\n')

file_w.writelines(lines_w)
file_w.close()
