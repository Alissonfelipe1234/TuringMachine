archiveIn = open("input.in","r")
input = archiveIn.readlines()
archiveIn.close()

cells = []
for read in input:
    cells = cells + list(read)

archive = open("code.turing","r")
code = [i for i in archive.readlines() if not str(i).startswith("//") and not str(i).startswith("\n")]

#the machine works here


out = open("output.out","w")
out.writelines(''.join(cells))
out.close()