print("Ingrese el máximo valor para x:")
while True:
    tope_x = int(input())
    if tope_x >= 0:
        break

paso_x = 0
while True:
    if paso_x <= tope_x:
        resultado_polinomio = paso_x ** 3 + paso_x ** 2 - 5
        print("Para x =", paso_x, "f(x) =", resultado_polinomio)
        paso_x = paso_x + 2
    if paso_x > tope_x:
        break
