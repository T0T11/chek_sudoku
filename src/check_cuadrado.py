def check_cuadrado(sudoku):

    if not sudoku or not all(sudoku): return False
    num_filas = len(sudoku)

    for fila in sudoku:
        if num_filas != len(fila): return False

    return True

if __name__ == '__main__':


    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_cuadrado(correcto) is True

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    assert check_cuadrado(numero_repetido_fila_columna) is True

    numero_repetido_columna =   [[1, 2, 3],
                                 [2, 3, 1],
                                 [2, 3, 1]]

    assert check_cuadrado(numero_repetido_columna) is True

    numero_no_presente =    [[1, 2, 3, 4],
                             [2, 3, 1, 2],
                             [4, 1, 2, 3],
                             [2, 3, 1, 4]]

    assert check_cuadrado(numero_no_presente) is True

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]

    assert check_cuadrado(numero_fuera_del_rango) is False

    caracteres = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    assert check_cuadrado(caracteres) is True

    numeros_reales =    [[1, 1.5],
                         [1.5, 1]]

    assert check_cuadrado(numeros_reales) is True

    irregular_fila =    [[1, 2, 3],
                         [2, 3, 1]]

    assert check_cuadrado(irregular_fila) is False

    irregular_columna = [[1, 2, 3],
                         [2, 3, 1],
                         [3, 1]]

    assert check_cuadrado(irregular_columna) is False

    lista_vacia = [[]]

    assert check_cuadrado(lista_vacia) is False
