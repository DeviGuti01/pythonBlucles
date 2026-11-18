entrada = int(input("digite un numero: "))

if entrada > 0:
    resto_numero = entrada
    digito = 0
    acumulador = 0
    total_digitos = 0
    while resto_numero > 0:
        digito = resto_numero % 10
        resto_numero = resto_numero // 10
        acumulador = acumulador + digito
        total_digitos = total_digitos + 1
    print("La cantidad de cifras de:", entrada, "son", total_digitos)
    print("La sumatoria es:", acumulador)
else:
    print("El numero no es positivo")
