import numpy as np

print("Hello world")
Cx = 0.0; Cy = 0.0; Cz = 0.0; Teta = 0.0; Rad = 0.0

def GetValues(Cx, Cy, Cz, Teta, Rad):
    print("Ingresa los valores de las coordendas")
    Cx = float (input("Valor de X:"))
    Cy = float (input("Valor de Y:"))
    Cz = float (input("Valor de Z:"))
    Teta = float (input("Ángulo a rotar:"))
    Rad = np.deg2rad(Teta)
    return Cx, Cy, Cz, Teta, Rad

def ConvertToArray(Cx, Cy, Cz):
    P = np.array([Cx, Cy, Cz])
    return P

def SelectAxis():
    axis = input("¿En base a que eje se hará la rotación? ")
    return axis

def say():
    print("[",Cx,",",Cy,",",Cz,",",Teta,",",Rad,"]")

def ProcessRx(p,teta):
    teta = np.deg2rad(Teta)
    Rx = np.array([[1,0,0],
                  [0, np.cos(teta), -np.sin(teta)],
                  [0, np.sin(teta), np.cos(teta)]])
    return Rx @ p

def ProcessRy(p, teta):
    Ry = np.array([[np.cos(teta),0,np.sin(teta)],
                  [0, 1, 0],
                  [-np.sin(teta), 0, np.cos(teta)]])
    return Ry @ p

def ProcessRz(p, teta):
    Rz = np.array([[np.cos(teta), -np.sin(teta), 0],
                  [np.sin(teta), np.cos(teta), 0],
                  [0, 0, 1]])
    return Rz @ p

def main(): 
    Cx, Cy, Cz, Teta, Rad = GetValues(Cx, Cy, Cz, Teta, Rad)
    P = ConvertToArray(Cx, Cy, Cz)
    axis = SelectAxis
    match axis:
        case "X":
            result = ProcessRx(P, Rad)
        case "Y":
            result = ProcessRy(P, Rad)
        case "Z":
            result = ProcessRz(P, Rad)
    