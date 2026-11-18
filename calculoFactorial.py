n_ingresado = int(input("Ingrese un número: "))
if n_ingresado < 0:
    print("el número no posee factorial.")
else:
    resultado_fact = 1
    multiplicador = 1
    while True:
        if n_ingresado > 0:
            resultado_fact = resultado_fact * multiplicador
            multiplicador = multiplicador + 1
        if multiplicador > n_ingresado:
            break
    print("El factorial de", n_ingresado, "es:", resultado_fact)
