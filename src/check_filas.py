def check_filas(sudoku):

    if not sudoku or not all(sudoku): return False
    numero_maximo = max(len(fila) for fila in sudoku)
    fila_correcta = list(range(1, numero_maximo + 1))

    for fila in sudoku:
        if sorted(fila) != fila_correcta: return False

    return True

if __name__ == '__main__':


    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_filas(correcto) is True

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    assert check_filas(numero_repetido_fila_columna) is False

    numero_repetido_columna =   [[1, 2, 3],
                                 [2, 3, 1],
                                 [2, 3, 1]]

    assert check_filas(numero_repetido_columna) is True

    numero_no_presente =    [[1, 2, 3, 4],
                             [2, 3, 1, 2],
                             [4, 1, 2, 3],
                             [2, 3, 1, 4]]

    assert check_filas(numero_no_presente) is False

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]

    assert check_filas(numero_fuera_del_rango) is False

    irregular_fila =    [[1, 2, 3],
                         [2, 3, 1]]

    assert check_filas(irregular_fila) is True

    irregular_columna = [[1, 2, 3],
                         [2, 3, 1],
                         [3, 1]]

    assert check_filas(irregular_columna) is False

    sudoku_con_lista_vacia = [[],
                             [1, 2, 3],
                             [2, 3, 1]]

    assert check_filas(sudoku_con_lista_vacia) is False

    sudoku_vacio = [[]]

    assert check_filas(sudoku_vacio) is False
