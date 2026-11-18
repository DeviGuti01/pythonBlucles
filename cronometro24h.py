reloj_horas = 0
while True:
    reloj_minutos = 0
    while True:
        reloj_segundos = 0
        while True:
            print(reloj_horas, ":", reloj_minutos, ":", reloj_segundos, sep="")
            reloj_segundos = reloj_segundos + 1
            if segundero > 59:
                break
        reloj_minutos = reloj_minutos + 1
        if reloj_minutos > 59:
            break
    reloj_horas = reloj_horas + 1
    if reloj_horas > 23:
        break
