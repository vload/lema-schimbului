"""
programul citeste din fisierul input.txt

daca folosim notatiile

L = SLI
S = SG

l = cardinalul lui L
s = cardinalul lui S

L = {v1, v2, ..., vl}
S = {w1, w2, ..., ws}

vi sau wi sunt scrise orizontal cu spatii intre numere, spre ex:
0 12 5.3 1

fisierul input.txt trebuie formatat astfel

n
l
s
v1
v2
...
vl
w1
w2
...
ws
"""

from copy import deepcopy

def esalon(array):
    i = 0
    solved = 0
    while i < len(array) and solved < len(array[i]):
        for j in range(solved, len(array[i])):
            if array[i][j] != 0:
                if j is not solved:                          #interschimbarea liniilor
                    for k in range(len(array)):
                        array[k][solved], array[k][j] = array[k][j], array[k][solved]
                
                if array[i][solved] is not 1:                #impartire la array[i][i]
                    factor = array[i][solved]
                    for k in range(len(array)):
                        array[k][solved] = array[k][solved] / factor
                
                for l in range(len(array[i])):
                    if l is not solved:
                        factor = array[i][l]
                        if factor:
                            for k in range(len(array)):
                                array[k][l] = array[k][l] - array[k][solved] * factor
                
                solved = solved + 1
                break
        i = i + 1
    return array

if(__name__ == "__main__"):
    print(__doc__)

    n = l = s = 0
    L = []
    S = []

    with open("input.txt") as f:
        n = int(f.readline())
        l = int(f.readline())
        s = int(f.readline())

        for i in range(l):
            temp = f.readline().split()
            temp = list(map(float, temp))
            L.append(temp)
        
        for i in range(s):
            temp = f.readline().split()
            temp = list(map(float, temp))
            S.append(temp)

    replaced = []
    for vi in L:
        es = esalon(deepcopy(S + [vi]))
        pos = -1
        for i in range(len(es[-1])):
            if es[-1][i]:
                pos = -1
                for j in range(len(es) - 1):
                    if es[j][i]:
                        pos = j
                if pos is not -1:
                    break
        S[pos] = vi
    print(S)
