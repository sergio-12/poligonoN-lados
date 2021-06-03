import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image
plt.imshow(Image.open('fondo.png'))
array = []


def Bresenham(x1, y1, x2, y2):
    
    dx = x2 - x1
    dy = y2 - y1

    xinc = 1 if dx > 0 else -1
    yinc = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xinc, 0, 0, yinc
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, yinc, xinc, 0

    dx1 = 2*dy - dx
    dy1 = 0

    for x in range(dx + 1):
        yield x1 + x*xx + dy1*yx, y1 + x*xy + dy1*yy
        if dx1 >= 0:
            dy1 += 1
            dx1 -= 2*dx
        dx1 += 2*dy

def arrayfill(start, center, base):  
    gradosI=0
    x1, y1 = center
    x2, y2 = base 
    for n in range(start):
        array.append([])
        print(math.degrees(gradosI))
        for j in range(2): 
            if j == 0:
                valor = round((x1+math.cos(gradosI)*(x2 - x1)-math.sin(gradosI) * (y2 - y1)))
                array[n].append(valor)
            else: 
                valor = round((y1 + math.sin(gradosI) * (x2 - y1) + math.cos(gradosI)  * (y2 - y1)))
                array[n].append(valor)
        gradosI += math.radians(360/start)

def pixel(start):
    resultado=[]
    for n in range(start):
        if n == L-1:
            puntos = list(Bresenham(array[n][0], array[n][1], array[0][0], array[0][1]))
            resultado+=puntos

        else:
            puntos = list(Bresenham(array[n][0], array[n][1], array[n+1][0], array[n+1][1]))
            resultado+=puntos
            
    for i in resultado:
        plt.gca().add_patch(Rectangle((i), 1, 1, linewidth=1, edgecolor='red', facecolor='none'))
        plt.ylim(0, 50)
        


if __name__ == "__main__": 
    x2 = int(input("Ingrese la Longitud de la figurs: "))
    L= int(input("introduce el numero de lados=: "))   
    x1 = 1
    y1 = 1
    base= (x1+x2, y1)
    origen = (x1, y1)
    arrayfill(L, origen, base)
    pixel(L)
    print(array)
    plt.title('Digital Differential Analyzer')
    plt.xlim([-1, 20])
    plt.ylim([-1, 20])
    plt.show()