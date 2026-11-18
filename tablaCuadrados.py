print("Ingrese la cantidad de números:")
while True:
    limite_tabla = int(input())
    if limite_tabla >= 0:
        break

base = 1
while True:
    if base <= limite_tabla:
        print(base, " ", base * base, " ", base_sumando + base * base, sep="")
        siguiente_base = base + 1
    if base > limite_tabla:
        break
