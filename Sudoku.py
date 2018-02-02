import copy

# Devuelve un booleano en funcion de si es factible posicionar el numero pasado en las coordenadas también pasadas
# Returns a Boolean according to whether it is possible to position the last number in the coordinates also passed
def factible(solucion, posicionFila, posicionColumna,posibleSolucion):
    valido=True

    #Comprobar coincidencia en fila
    #Check match in row
    i=0
    while i<9 and valido==True:
        if i!=posicionFila:
            if solucion[i][posicionColumna]==posibleSolucion:
                valido=False
        i=i+1

    # Comprobar coincidencia en columna
    # Check column match
    if valido:
        i=0
        while i<9 and valido==True:
            if i != posicionColumna:
                if solucion[posicionFila][i] == posibleSolucion:
                    valido = False
            i=i+1

        # Comprobar coincidencia en submatriz
        # Check match in sub-matrix
        if valido:
            inicioSubmatrizFila = (int(posicionFila / 3)) * 3
            inicioSubmatrizColumna = (int(posicionColumna / 3)) * 3

            i=inicioSubmatrizFila
            while i<inicioSubmatrizFila+3 and valido==True:
                j=inicioSubmatrizColumna
                while j < inicioSubmatrizColumna + 3 and valido == True:
                    if posibleSolucion == solucion[i][j]:
                        valido = False
                    j=j+1
                i=i+1

    return valido


# Imprime el sudoku
# Prints the sudoku
def imprimirSudoku(soluciones):
    for i in soluciones:
        for j in i:
            print(j)
        print("\n")



#Soluciona el sudoku pasado mediante backtracking
#Solve the sudoku by backtracking
def solucionadorSudoku(sudoku, solucion, posicionFila, posicionColumna,soluciones):
    # Si el valor del número del sudoku que se está evaluando es 0, se crearán los casos con las posibles soluciones, sino se pasará al siguiente número
    # If the value of the number being evaluated is 0, the cases with the possible solutions will be created, otherwise it will pass to the next number
    if sudoku[posicionFila][posicionColumna]==0:
        for i in range(1,10):
            if factible(solucion, posicionFila, posicionColumna, i):
                solucion[posicionFila][posicionColumna]=i

                if posicionFila==8 and posicionColumna==8:
                    soluciones.append(copy.deepcopy(solucion))
                else:
                    if posicionColumna==8:
                        solucionadorSudoku(sudoku, solucion, posicionFila+1, 0,soluciones)
                    else:
                        solucionadorSudoku(sudoku, solucion, posicionFila,posicionColumna+1,soluciones)
                solucion[posicionFila][posicionColumna] = 0
    else:
        if posicionFila == 8 and posicionColumna == 8:
            soluciones.append(copy.deepcopy(solucion))
        else:
            if posicionColumna == 8:
                solucionadorSudoku(sudoku, solucion, posicionFila + 1, 0,soluciones)
            else:
                solucionadorSudoku(sudoku, solucion, posicionFila, posicionColumna + 1,soluciones)



"""
sudoku=[[1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
"""

sudoku=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,0,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,0,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


solucion=copy.deepcopy(sudoku)
soluciones=[]
solucionadorSudoku(sudoku,solucion,0,0,soluciones)

print(len(soluciones))
imprimirSudoku(soluciones)
