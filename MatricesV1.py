import numpy as np

print("Hello world")
Cx = 0.0; Cy = 0.0; Cz = 0.0; Teta = 0.0

def main():
    print("Ingresa los valores de las coordendas")
    global Cx
    Cx = float (input("Valor de X:"))
    global Cy
    Cy = float (input("Valor de Y:"))
    global Cz
    Cz = float (input("Valor de Z:"))
    global Teta
    Teta = float (input("Ángulo a rotar:"))

    P = np.array([Cx, Cy, Cz])

    result = processRx(P)
    say()
    print(result)

def say():
    print("[",Cx,",",Cy,",",Cz,",",Teta,"]")

def processRx(p):
    teta = np.deg2rad(Teta)
    Rx = np.array([[1,0,0],
                  [0, np.cos(teta), -np.sin(teta)],
                  [0, np.sin(teta), np.cos(teta)]])
    return Rx @ p


def processRy(p):
    Ry = np.array([[np.cos(teta),0,np.sin(teta)],
                  [0, 1, 0],
                  [-np.sin(teta), 0, np.cos(teta)]])
    return Ry @ p

def processRz(p):
    Rz = np.array([[np.cos(teta), -np.sin(teta), 0],
                  [np.sin(teta), np.cos(teta), 0],
                  [0, 0, 1]])
    return Rz @ p
    
main()
