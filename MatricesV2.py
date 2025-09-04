import numpy as np

def GetValues():
    """
    Obtiene los valores del punto, el angulo y convierte a radianes.

    Parameters:
        No tiene ningun parámetro

    Returns:
        Cx(float): Punto ubicado en la coordenada X.
        Cy(float): Punto ubicado en la coordenada Y.
        Cz(float): Punto ubicado en la coordenada Z.
        Teta(float): Valor de los grados a rotar.
        Rad(float): Guarda el valor de la conversion de grados a radianes

    """
    print("Ingresa los valores de las coordendas")
    Cx = float (input("Valor de X:"))
    Cy = float (input("Valor de Y:"))
    Cz = float (input("Valor de Z:"))
    Teta = float (input("Ángulo a rotar:"))
    Rad = np.deg2rad(Teta)
    return Cx, Cy, Cz, Rad

def rot_x(p,teta):
    """
    Realiza la rotacion en el eje X

    Parámetros:
        p(array): Arreglo con las coordenadas del punto del vector.
        teta(float): Contiene la rotación en radianes, se usa teta como nombre por comodidad.
    
    Returns:
        (array): Regresa el resultado de la multiplicación del vector del punto y la matriz respectiva del eje.
    """
    Rx = np.array([[1,0,0],
                  [0, np.cos(teta), -np.sin(teta)],
                  [0, np.sin(teta), np.cos(teta)]])
    return Rx @ p

def rot_y(p, teta):
    """
    Realiza la rotacion en el eje Y

    Parámetros:
        p(array): Arreglo con las coordenadas del punto del vector.
        teta(float): Contiene la rotación en radianes, se usa teta como nombre por comodidad.
    
    Returns:
        (arrray): Regresa el resultado de la multiplicación del vector del punto y la matriz respectiva del eje.
    """
    Ry = np.array([[np.cos(teta),0,np.sin(teta)],
                  [0, 1, 0],
                  [-np.sin(teta), 0, np.cos(teta)]])
    return Ry @ p

def rot_z(p, teta):
    """
    Realiza la rotacion en el eje Z

    Parámetros:
        p(array): Arreglo con las coordenadas del punto del vector.
        teta(float): Contiene la rotación en radianes, se usa teta como nombre por comodidad.
    
    Returns:
        (array): Regresa el resultado de la multiplicación del vector del punto y la matriz respectiva del eje.
    """
    Rz = np.array([[np.cos(teta), -np.sin(teta), 0],
                  [np.sin(teta), np.cos(teta), 0],
                  [0, 0, 1]])
    return Rz @ p

def rotar(P, axis, Rad):
    """
    Seleciona el eje proporcionado por el usuario.

    Parámetros:
        P(array): Arreglo con las coordenadas del punto del vector.
        axis(string): Contiene el eje a utilizar.
        Rad(float): Contiene la conversion de grados a radianes.

    Returns:
        (array): El vector resultante despues de aplicar la matriz de rotación.
    """
    match axis:
        case "X":
            result = rot_x(P, Rad)
        case "Y":
            result = rot_y(P, Rad)
        case "Z":
            result = rot_z(P, Rad)
        case _:
            print("Opcion no válida, intenta de nuevo")
    return result

def main(): 
    """
    Es el metodo principal y el origen de la ejecución.

    Parámetros:
        No tiene ningun parametro.

    Return:
        No devuelve ningun valor. 
    """
    Cx, Cy, Cz, Rad = GetValues()
    P = np.array([Cx, Cy, Cz])
    axis = input("¿En base a que eje se hará la rotación? ")
    result = rotar(P, axis, Rad)
    print("El resultado es: ", np.round(result, 2))

main()