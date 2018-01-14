import numpy as np


r = np.random.randint(low=3,high=4)
print "this is r:"
print r
A = np.random.randint(low=-10,high=10,size=(r,r))
print "this is A:"
print A 
b = np.arange(r).reshape((r,1))
print "this is b:"
print b


def augmentMatrix(A, b):
    res=[['0']*(len(A[0])+1) for i in range(len(A))]
    for y in range(len(A)):
        for x in range(len(A[0])):
            res[y][x] = A[y][x]
    for y in range(len(b)):
        res[y][len(A[0])] = b[y][0]
    return res
def swapRows(M, r1, r2):
    M[r1],M[r2]=M[r2],M[r1]

def scaleRow(M, r, scale):
    try:
        print M
        print "this is scale in scaleRow function : ->",scale
        if not M or scale == 0:
            raise ValueError
        for x in range(len(M[r])):
            M[r][x] = scale*M[r][x]
    except ValueError:
        raise ValueError("plz input valid parameter: Matrix, rownum, scalanumber")


def addScaledRow(M, r1, r2, scale):
    try:
        #r1 is the row to be added
        if not M or scale == 0:
            raise ValueError
        for x in range(len(M[r1])):
            M[r1][x] = M[r1][x]+scale*M[r2][x]
    except ValueError:
        raise ValueError("plz input valid parameter: Matrix, rownum, scalanumber")
        



def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    if not len(A)==len(A[0]) or not len(b[0])==1 or not len(A)==len(b):
        return None
    augmentedMtx = augmentMatrix(A, b)
    print augmentedMtx
    for c in range(len(A)):
        print "this is c in range(len(A)) ==> ",c
        for j in range(c+1,len(A)):
            print " this is j under c loop: --> ",j
            if augmentedMtx[c][c]<augmentedMtx[j][c]:
                print "augmentedMtx[i][c]<augmentedMtx[j][c]",augmentedMtx[c][c],augmentedMtx[j][c]
                augmentedMtx[c],augmentedMtx[j]=augmentedMtx[j],augmentedMtx[c]
                print augmentedMtx
        if abs(augmentedMtx[c][c]) < epsilon:
            return None
        print "beta value = 1/augmentedMtx[c][c]: --> ",augmentedMtx[c][c]
        beta = 1.0000/augmentedMtx[c][c]
        scaleRow(augmentedMtx,c,beta)
        for j in range(len(A)):
            if j == c:
                continue
            beta = -(augmentedMtx[j][c])
            print "this is beta to be input in addScaledRow ++> ",beta
            addScaledRow(augmentedMtx,j,c,beta)
        print augmentedMtx
        #clear coefficient below

    print augmentedMtx            
    res =[]
    for i in range(len(augmentedMtx)):
        a = round(augmentedMtx[i][len(augmentedMtx)],4)
        res.append(a)
    print res










gj_Solve(A,b)