from functools import reduce
def sumatoria(lista,new_lista = 0):
    if lista:
        suma = new_lista + lista[0]
        return sumatoria(lista[1:],suma)
    return new_lista
def productoria(lista,new_lista = 1):
    if lista:
        suma = new_lista * lista[0]
        return productoria(lista[1:],suma)
    return new_lista
def operacion(operador):
    if operador == "+":
        def calcularSumatoria(matriz):
            suma = 0
            for fila in matriz:
                if matriz.index(fila)%2 == 0:
                    continue
                else:
                    suma += sumatoria(fila)
            return suma 

        return calcularSumatoria
    if operador == "-":
        def calcularProductoria(matriz):
            producto = 1
            i = 0
            columna = []
            while i <len(matriz[0]):
                if not i%2==0:
                    for fila in matriz:
                        columna.append(fila[i])
                    producto += productoria(columna)
                    
                i+=1  
            return producto     
        return calcularProductoria
def diferenciaMatriz(matriz):
    sumato = operacion("+")
    producto = operacion("-")
    return sumato(matriz)-producto(matriz)
def iguales(lista1,lista2):
    iterable = iter(lista2)
    nuevalista = list(filter(lambda x:x==next(iterable), lista1))
    return nuevalista
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(diferenciaMatriz(matriz))
        
