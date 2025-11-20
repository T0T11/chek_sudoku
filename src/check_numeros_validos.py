def check_numeros_validos(sudoku):

    assert isinstance(sudoku, list), 'el sudoku tiene que ser una lista'
    if not sudoku or not all(sudoku): return False
    numero_maximo = max(len(fila) for fila in sudoku)
    if len(sudoku) > numero_maximo: numero_maximo = len(sudoku)

    for fila in sudoku:
        for valor in fila:
            if valor not in range(1, numero_maximo + 1): return False

    return True

if __name__ == '__main__':


    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_numeros_validos(correcto) is True

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    assert check_numeros_validos(numero_repetido_fila_columna) is True

    numero_repetido_columna =   [[1, 2, 3],
                                 [2, 3, 1],
                                 [2, 3, 1]]

    assert check_numeros_validos(numero_repetido_columna) is True

    numero_no_presente =    [[1, 2, 3, 4],
                             [2, 3, 1, 2],
                             [4, 1, 2, 3],
                             [2, 3, 1, 4]]

    assert check_numeros_validos(numero_no_presente) is True

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]

    assert check_numeros_validos(numero_fuera_del_rango) is False

    caracteres = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    assert check_numeros_validos(caracteres) is False

    numeros_reales =    [[1, 1.5],
                         [1.5, 1]]

    assert check_numeros_validos(numeros_reales) is False

    irregular_fila =    [[1, 2, 3],
                         [2, 3, 1]]

    assert check_numeros_validos(irregular_fila) is True

    irregular_columna = [[1, 2, 3],
                         [2, 3, 1],
                         [3, 1]]

    assert check_numeros_validos(irregular_columna) is True

    lista_vacia = [[]]

    assert check_numeros_validos(lista_vacia) is False
