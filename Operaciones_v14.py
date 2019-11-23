import numpy as np
import math
def suma(m1, m2):
    r1 = m1[0] + m2[0]
    r2 = m1[1] + m2[1]
    r = [r1, r2]
    return r
def conjugado(z):
    w = [z[0], -z[1]]
    return w
def prod(m1, m2):
    r1 = m1[0] * m2[0] - m1[1] * m2[1]
    r2 = m1[0] * m2[1] + m2[0] * m1[1]
    r = [r1, r2]
    return r

def columna(j, W):
    Z = [0]*len(W)
    k = 0
    for i in W:
        Z[k] = [i[j]]
        k = k+1
    return Z

def modul(a1):
    r1 = math.sqrt(a1[0] ** 2 + a1[1] ** 2)
    r = round(r1,2)
    return r


def fila_por_columna(V, W):
    t = [0, 0]
    for i in range(len(V)):
        t = suma(t, prod(V[i], W[i][0]))
    return t

def producto_de_matrices(A, B):
    f = len(A)
    c = len(B[0])
    C = [[0]*c for fila in range(f)]
    for i in range(f):
        for j in range(c):
            C[i][j] = fila_por_columna(A[i], columna(j, B))
    return C

def producto_tensorial(A, B):
    f_A = len(A)
    c_A = len(A[0])
    f_B = len(B)
    c_B = len(B[0])
    f_T = f_A * f_B
    c_T = c_A * c_B
    T = [[0]*c_T for fila in range(f_T)]
    for i in range(f_T):
        for j in range(c_T):
            T[i][j] = prod(A[i // f_B][j // c_B], B[i % f_B][j % c_B])
    return T

def vec(complejo):
    if "+" in complejo[1:] or "-" in complejo[1:] :
        if complejo[0] == "-":
            L = 1
            oper = complejo[1:]
        else:
            L = 0
            oper = complejo[:]
        for letra in oper:
            if letra == "+" or letra == "-":
                a1 = complejo[:L]
                b1 = complejo[L:]
                b1 = b1[1:-1]
                if b1 == '':
                    b1 = 1
                
                if letra == "-":
                    r = [round(float(a1), 2),-round(float(b1), 2)]
                else:
                    r = [round(float(a1), 2),round(float(b1), 2)]
            L += 1
            
    else:
        if "i" in complejo:
            if complejo == "i" or complejo == "-i":
                if complejo == "i":
                    r = [0, 1]
                else:
                    r = [0,-1]
            else:
                r = [0, round(float(complejo[:-1]), 2)]
        else:
            r = [round(float(complejo), 2), 0]
    return r

def compl(v):
    if v[0] != 0 and v[1] != 0:
        if v[1] < 0:
            r = str(v[0]) + " " + str(v[1]) +"i"
        else:
            r = str(v[0]) + " + " + str(v[1]) +"i"
    elif v[0] == 0 and v[1] != 0:
        r = str(v[1]) + "i"
    elif v[0] != 0 and v[1] == 0:
        r =  str(v[0])
    elif v[0] == 0 and v[1] == 0:
        r = str(0)
    return r

def M_u(M1):
    if M1 == []:
        r = []
        return False
    else:
        x1 = len(M1)
        y1 = len(M1[0])
        if y1 == x1:
            r = Mult_M(M1, M1)
            zero = 0
            one = 0
            for i in range(x1):
                for x in range(y1):
                    if r[i][x] == "0":
                        zero += 1
                    elif r[i][x] == "1.0i":
                        one += 1
            if zero == x1**2 - x1 and one == x1:
                return True
            else:
                return False
        else:
            return False
def mult_cM(c, M):
    M_r = []
    if M == []:
        return []
    else:
        x = len(M)
        y = len(M[0])
        for i in range(x):
            M_r.append([])
            for j in range(y):
                m = prod(c, M[i][j]) 
                M_r[i].append(m)
        return M_r
def norma(V):
    n = np.sqrt(producto_interno(V, V))
    return n[0]
def producto_interno(V, W):
    Z = producto_de_matrices(adjunta(V), W)
    return Z[0][0]
def adjunta(A):
    B = conjugada(transpuesta(A))
    return B
def transpuesta(A):
    f = len(A)
    c = len(A[0])
    B = [[0]*f for fila in range(c)]
    for i in range(c):
        for j in range(f):
            B[i][j] = A[j][i]
    return B

def conjugada(A):
    f = len(A)
    c = len(A[0])
    B = [[0]*c for fila in range(f)]
    for i in range(f):
        for j in range(c):
            B[i][j] = conjugado(A[i][j])
    return B
def sumaM(A, B):
    f = len(A)
    c = len(A[0])
    C = [[0]*c for fila in range(f)]
    for i in range(f):
        for j in range(c):
            C[i][j] = suma(A[i][j], B[i][j])
    return C

def modulo(z):
    """
    Devuelve un número igual al módulo de un número complejo
    """
    r = np.sqrt(prod(z, conjugado(z)))
    return r[0]
def pol(z):
    Rho = modulo(z)
    Theta = np.arctan2(z[1],z[0])
    p = [Rho, Theta]
    return p
    
