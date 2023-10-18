data = open("input.txt").read().splitlines()
 
wires={}
 
AND = ' AND '
OR = ' OR '
LSHIFT = ' LSHIFT '
RSHIFT = ' RSHIFT '
NOT = 'NOT'
 
for d in data:
    signal, wire = d.split(' -> ')
    wires[wire] = signal
# print(wires)
 
def solve(wire):    
    if wire.isnumeric():
        return int(wire)
 
    signal = wires[wire]
 
    if type(signal) == int or signal.isnumeric():
        wires[wire] = int(signal)
 
    else:
        if AND in signal:
            a, b = signal.split(AND)
            wires[wire] = solve(a) & solve(b)
 
        elif OR in signal:
            a, b = signal.split(OR)
            wires[wire] = solve(a) | solve(b)
 
        elif LSHIFT in signal:
            a, b = signal.split(LSHIFT)
            wires[wire] = solve(a) << int(b)
 
        elif RSHIFT in signal:
            a, b = signal.split(RSHIFT)
            wires[wire] = solve(a) >> int(b)
 
        elif NOT in signal:
            _, a = signal.split()
            wires[wire] = ~(solve(a))
 
        else:
            wires[wire] = solve(signal)
 
    return wires[wire]
 

print(solve('a'))

tmp = solve('a')
for d in data:
    signal, wire = d.split(' -> ')
    wires[wire] = signal
wires['b']= tmp
print(solve('a'))