def check_columnas(sudoku):

    if not sudoku or not all(sudoku): return False
    numero_maximo = len(sudoku)
    columna_correcta = list(range(1, numero_maximo + 1))

    for i in range(numero_maximo):
        columna = [fila[i] for fila in sudoku if i < len(fila)]
        if sorted(columna) != columna_correcta: return False

    return True

if __name__ == '__main__':


    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_columnas(correcto) is True

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    assert check_columnas(numero_repetido_fila_columna) is False

    numero_repetido_columna =   [[1, 2, 3],
                                 [2, 3, 1],
                                 [2, 3, 1]]

    assert check_columnas(numero_repetido_columna) is False

    numero_no_presente =    [[1, 2, 3, 4],
                             [2, 3, 1, 2],
                             [4, 1, 2, 3],
                             [2, 3, 1, 4]]

    assert check_columnas(numero_no_presente) is False

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]

    assert check_columnas(numero_fuera_del_rango) is False

    caracteres = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    assert check_columnas(caracteres) is False

    numeros_reales =    [[1, 1.5],
                         [1.5, 1]]

    assert check_columnas(numeros_reales) is False

    irregular_fila =    [[1, 2, 3],
                         [2, 3, 1]]

    assert check_columnas(irregular_fila) is False

    irregular_columna = [[1, 2, 3],
                         [2, 3, 1],
                         [3, 1]]

    assert check_columnas(irregular_columna) is False

    lista_vacia = [[]]

    assert check_columnas(lista_vacia) is False
