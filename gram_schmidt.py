#!/usr/bin/env python

"""
Calcula la factorización de gram-schmidt
para una matriz de tamaño n
"""


def dot(x: list[float], y: list[float]) -> float:
    """Producto punto entre dos vectores"""
    dot = [xi * yi for xi, yi in zip(x, y)]
    return sum(dot)


def transpose(M: list[list[float]]) -> list[list[float]]:
    """Devuelve traspuesta de una matriz"""
    return [[M[i][j] for i in range(len(M))] for j in range(len(M))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Multiplicación de dos matrices"""
    ...


def matvec(A: list[list[float]], v: list[float]) -> list[float]:
    """Multiplicación de matriz por un vector"""


def norm(x: list[float]) -> float:
    """Obtiene la norma 2 de un vector"""
    ...


def proj(u: list[float], v: list[float]) -> list[float]:
    """Calcula la proyección de u en v"""
    ...


def normalize(u: list[float]) -> list[float]:
    """Normaliza un vector"""
    ...


def matrix_to_str(matrix: list[list[float]]) -> str:
    """Convierte una matriz a texto"""
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    # return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])
    return "\n".join(table)


def main():
    x, y = [1, 2, 3], [4, 5, 6]
    punto = dot(x, y)
    print(punto)
    matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    trans = transpose(matrix)
    print(trans)


main()

