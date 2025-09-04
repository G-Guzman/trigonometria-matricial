import numpy as np


def rot_x(x, y, z, theta):
    '''
    Descripcion
        Rotates the vector in the X axis.

    Parameters:
        x (float): Value of the vector in X
        y (float): Value of the vector in Y
        z (float): Value of the vector in Z
        theta (float): Value of the angle, in radians.

    Returns:
        array: The result of the multiplication of the vector and the matrix.
    '''
    p = np.array([x, y, z])
    Rx = np.array([[1,0,0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    return Rx @ p

def rot_y(x, y, z, theta):
    '''
    Descripcion
        Rotates the vector in the Y axis.
        
    Parameters:
        x (float): Value of the vector in X
        y (float): Value of the vector in Y
        z (float): Value of the vector in Z
        theta (float): Value of the angle, in radians.

    Returns:
        array: The result of the multiplication of the vector and the matrix.
    '''
    p = np.array([x, y, z])
    Ry = np.array([[np.cos(theta),0,np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    return Ry @ p

def rot_z(x, y, z, theta):
    '''
    Descripcion
        Rotates the vector in the Z axis.
        
    Parameters:
        x (float): Value of the vector in X
        y (float): Value of the vector in Y
        z (float): Value of the vector in Z
        theta (float): Value of the angle, in radians.

    Returns:
        array: The result of the multiplication of the vector and the matrix.
    '''
    p = np.array([x, y, z])
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return Rz @ p


def rotar(x, y, z, theta, axis):
    '''
    Descripcion

    Parameters:
        x (float): Value of the vector in X
        y (float): Value of the vector in Y
        z (float): Value of the vector in Z
        theta (float): Value of the angle to rotate
        axis (string): The rotation axis. Only can be "X", "Y", "Z" in capital letters

    Returns:
        The funtion doesn't return anything
    '''
    Rad = np.deg2rad(theta)

    match axis:
        case "X":
            result = rot_x(x, y, z, Rad)
        case "Y":
            result = rot_y(x, y, z, Rad)
        case "Z":
            result = rot_z(x, y, z, Rad)
        case _:
            print("Opcion de eje no válida, intenta de nuevo")
            exit()
    print("El resultado es: ", np.round(result, 2))
    pass

x = 5; y = 5; z = 5; theta = 129; axis = "X" 
rotar(x, y, z, theta, axis)
