import math
def main():
    #escribe tu código abajo de esta línea
    area=float(input("Area a pintar en metros:"))
    rendimiento=float(input("Rendimiento (m2/l):"))
    litros=area/rendimiento
    print("Litros a comprar:",round(litros))

if __name__ == '__main__':
    main()
