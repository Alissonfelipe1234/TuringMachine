from State import State

archiveIn = open("input.in","r")
input = archiveIn.readlines()
archiveIn.close()

cells = []
reader = 0
states = []
end_states = []
for read in input:
    cells = cells + list(read)

archive = open("code.turing","r")
code = [i.replace('\n', ',\n').replace(' ', '').split(',') for i in archive.readlines() if not i.startswith("//") and not str(i).startswith("\n")]
archive.close()


current_state = states[0]

while current_state not in end_states:
    print('teste')    

out = open("output.out","w")
out.writelines(''.join(cells))
out.close()