from State import State

archiveIn = open("input.in","r")
input = archiveIn.readlines()
archiveIn.close()

cells = []
bico
states = []
end_states = ()
for read in input:
    cells = cells + list(read)

archive = open("code.turing","r")
code = [i.split(',') for i in archive.readlines() if not i.startswith("//") and not str(i).startswith("\n")]
archive.close()

for line in code:
    stateStatic = State(line[0])
    if stateStatic not in states:
        states.append(stateStatic)
    
current_state = states[0]


print(states)
#the machine works here


out = open("output.out","w")
out.writelines(''.join(cells))
out.close()