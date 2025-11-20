from src.check_cuadrado import check_cuadrado
from src.check_numeros_validos import check_numeros_validos
from src.check_filas import check_filas
from src.check_columnas import check_columnas

def check_sudoku(sudoku):

    return check_cuadrado(sudoku) and \
           check_numeros_validos(sudoku) and \
           check_filas(sudoku) and \
           check_columnas(sudoku)


if __name__ == '__main__':


    correcto = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2]]

    assert check_sudoku(correcto) is True

    numero_repetido_fila_columna = [[1, 2, 3, 4],
                                    [2, 3, 1, 3],
                                    [3, 1, 2, 3],
                                    [4, 4, 4, 2]]

    assert check_sudoku(numero_repetido_fila_columna) is False

    numero_repetido_columna =   [[1, 2, 3],
                                 [2, 3, 1],
                                 [2, 3, 1]]

    assert check_sudoku(numero_repetido_columna) is False

    numero_no_presente =    [[1, 2, 3, 4],
                             [2, 3, 1, 2],
                             [4, 1, 2, 3],
                             [2, 3, 1, 4]]

    assert check_sudoku(numero_no_presente) is False

    numero_fuera_del_rango =    [[1, 2, 3, 4, 5],
                                 [2, 3, 1, 5, 6],
                                 [3, 4, 5, 2, 1],
                                 [5, 6, 4, 3, 2]]

    assert check_sudoku(numero_fuera_del_rango) is False

    caracteres = [['a', 'b', 'c'],
                  ['b', 'c', 'a'],
                  ['c', 'a', 'b']]

    assert check_sudoku(caracteres) is False

    numeros_reales =    [[1, 1.5],
                         [1.5, 1]]

    assert check_sudoku(numeros_reales) is False

    irregular_fila =    [[1, 2, 3],
                         [2, 3, 1]]

    assert check_sudoku(irregular_fila) is False

    irregular_columna = [[1, 2, 3],
                         [2, 3, 1],
                         [3, 1]]

    assert check_sudoku(irregular_columna) is False

    lista_vacia = [[]]

    assert check_sudoku(lista_vacia) is False
